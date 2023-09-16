# RKBD
# Remote keyboard in python
# GitHub: https://www.github.com/lewisevans2007/rkbd
# Licence: GNU General Public License v3.0
# By: Lewis Evans

import socket
import time
import keyboard

from lib import banner
from lib import log

if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 5054
    banner.print_banner()
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    log.log("Your Computer Name is:" + hostname)
    log.log("Your Computer IP Address is:" + IPAddr)

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            while True:
                try:
                    server_socket.bind((ip, port))
                    log.success(f"Server bound to {ip}:{port}")
                    break
                except:
                    log.error("Port already in use! Waiting 2 seconds...")
                    time.sleep(2)
                    log.log("Restarting Server...")

            server_socket.listen()

            log.log("Server listening for connections...")
            conn, addr = server_socket.accept()
            with conn:
                log.success(f"Connected by: {addr}")
                data = conn.recv(1024)
                for i in data.decode().split("\n"):
                    if i.startswith("{{") and i.endswith("}}"):
                        log.success(f"Sleeping for {i[2:-2]} seconds")
                        time.sleep(float(i[2:-2]))
                    else:
                        log.log(f"Sending {i}")
                        try:
                            keyboard.press_and_release(i)
                        except ValueError:
                            keyboard.write(i)
                conn.sendall("OK".encode())
                conn.close()
        log.log("Connection closed")