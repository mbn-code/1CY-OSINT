 # Main file made for running with python3.10
import os
import sys
import platform
from time import sleep
import requests

version = "BETA-V1.10"

def main_script(command: str) -> None:
    match command.split():
        case ["version"]:
            print(f"Version: {version}")

        case ["ip" | "ipinfo", ip]:
            api_req = requests.get(f"https://ipinfo.io/{ip}")
            with open(f"Ip_information{ip}.txt", "w") as ip_info:
                ip_info.write(api_req.text)

        case _:
            print("Command currently not found")
            os.system(command)


def main():
    while 1:
        command = input(f"Hello, {platform.node()}: ")
        main_script(command)
    
if __name__ == "__main__":
    if platform == "linux" or "linux2" or "darwin":
            os.system("clear")
    elif platform == "win32":
        os.system("cls")
    else:
        pass

    words = "Welcome to 1CY-OSINT, the automated OSINT Toolkit for information gathering made easy\n"
    for char in words:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.020)

    main()