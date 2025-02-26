import os
import pkgutil
import subprocess


def get_installed_packages():
    """Get a list of installed packages using pip freeze."""
    try:
        installed_packages = subprocess.check_output(["pip", "freeze"], text=True).split("\n")
        return {pkg.split("==")[0]: pkg for pkg in installed_packages if "==" in pkg}
    except subprocess.CalledProcessError:
        print("Error retrieving installed packages.")
        return {}


def get_imported_modules():
    """Scan all Python files in the project and extract imported modules."""
    imported_modules = set()
    for root, _, files in os.walk("."):
        # Ignore virtual environments and hidden directories
        if any(ignored in root for ignored in [".venv", "venv", "__pycache__", ".git", ".idea"]):
            continue

        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("import ") or line.startswith("from "):
                            module = line.split()[1].split(".")[0]  # Get module name
                            imported_modules.add(module)

    return imported_modules


def generate_requirements():
    """Generate a requirements.txt file based on imported modules."""
    installed_packages = get_installed_packages()
    imported_modules = get_imported_modules()

    required_packages = set()

    for module in imported_modules:
        if module in installed_packages:
            required_packages.add(installed_packages[module])

    if required_packages:
        with open("requirements.txt", "w") as f:
            f.write("\n".join(sorted(required_packages)))
        print("✅ requirements.txt has been generated!")
    else:
        print("⚠️ No external dependencies found!")


if __name__ == "__main__":
    generate_requirements()
