import os            # Import the os module to interact with the operating system
import importlib     # Import the importlib module to import modules dynamically
import sys           # Import the sys module to access command-line arguments

COMMANDS_DIR = "commands"   # Set the directory where the command scripts are located

def list_commands():
    """List all available commands dynamically."""
    files = os.listdir(COMMANDS_DIR)   # Get a list of all files in the COMMANDS_DIR
    return [f[:-3] for f in files if f.endswith(".py") and f != "__init__.py"]
    # Return a list of filenames without the '.py' extension, excluding '__init__.py'

def load_command(command_name):
    """Dynamically load and execute a command."""
    try:
        module = importlib.import_module(f"{COMMANDS_DIR}.{command_name}")
        # Import the module with the given command name from the COMMANDS_DIR
        if hasattr(module, "run"):
            module.run(sys.argv[2:])  # If the module has a run() function, execute it with additional arguments
        else:
            print(f"Command '{command_name}' does not have a run() function.")
            # Print a message if the module doesn't have a run() function
    except ModuleNotFoundError:
        print(f"Command '{command_name}' not found.")
        # Print a message if the module cannot be found

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <command> [args]")
        # Print usage instructions if no command is given
        print("Available commands:", ", ".join(list_commands()))
        # List all available commands
        return

    command_name = sys.argv[1]
    # Get the command name from the first command-line argument
    load_command(command_name)
    # Load and execute the specified command

if __name__ == "__main__":
    main()
    # Call the main() function if this script is executed directly
