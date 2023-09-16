# RKBD
# Remote keyboard in python
# GitHub: https://www.github.com/lewisevans2007/rkbd
# Licence: GNU General Public License v3.0
# By: Lewis Evans

import socket
import sys

from lib import banner
from lib import log

if __name__ == "__main__":
    ip = None
    port = None
    filename = None
    for arg in sys.argv:
        if arg.startswith("--ip="):
            ip = arg[5:]
        elif arg.startswith("--port="):
            port = arg[7:]
        elif arg.startswith("--file="):
            filename = arg[7:]
    if ip is None or port is None or filename is None:
        print("Usage: python3 client.py --ip=<ip> --port=<port> --file=<file>")
        exit(1)
    port = int(port)
    banner.print_banner()

    log.log("Reading keystrokes from file...")
    keystrokes = open(filename, "r").read()
    log.success("Keystrokes read successfully!")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((ip, port))
        log.success("Connected to server!")
        client_socket.sendall(keystrokes.encode("UTF-8"))
        log.success("Keystrokes sent!")
        log.log("Waiting for response...")
        response = client_socket.recv(1024)
        log.success("Response received!")

    if response.decode() == "OK":
        log.success("Keystrokes sent successfully!")