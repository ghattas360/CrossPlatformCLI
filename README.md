# CrossPlatformCLI
Custom Command Line Interface (CLI) for IT &amp; System Engineers 🚀
This is a modular and extensible command-line tool designed for IT professionals and system engineers. 
It allows you to execute useful system commands on both Windows and Linux, 
such as checking disk space, retrieving IP information, listing running processes, and more...

The CLI supports dynamic command loading, 
meaning you can easily add, update, or remove commands without modifying the core script. 
Each command is stored as a separate Python file in the commands/ directory.

🔧 Features
✅ Cross-platform – Works on Windows & Linux
✅ Modular Design – Just drop new commands in the commands/ folder
✅ Useful Built-in Commands:

disk_usage → Check disk space
ip_info → Get IP address
process_list → List running processes
ping → Ping a host
network_status → Show active network connections
✅ Easy to Extend – Add more commands without changing the core
✅ No External Dependencies (Except psutil)


🚀 How to Use
1️⃣ Clone the repo:
      git clone https://github.com/ghattas360/CrossPlatformCLI.git cd mycli
      cd mycli

2️⃣ Install dependencies:
      pip install -r requirements.txt

3️⃣ Run the CLI:
      python cli.py

4️⃣ Execute commands:
      python cli.py disk_usage
      python cli.py ip_info
      python cli.py process_list
      python cli.py ping google.com




🛠️ How to Add a New Command
1️⃣ Create a new file inside the commands/ folder (e.g., new_command.py).
2️⃣ Define a run(args) function inside it.
3️⃣ The command will automatically be available! 🎯

Example:
    def run(args):
      print("Hello from my new command!")



🔗 Future Enhancements
Logging & history tracking
Automated system health checks
User authentication & role-based access
Cloud integration (e.g., AWS, Azure)
📌 Feel free to contribute and enhance this CLI! 🚀🔥

