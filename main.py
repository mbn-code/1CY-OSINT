 # Main file made for running with python3.10
import os
import sys
import platform
from time import sleep

version = "BETA-V1.10"

def main_script(command: str) -> None:
    match command.split(""):
        case ["version"]:
            print(f"Version: {version}")

        case ["ip" | "ipinfo", ip]:
            with open(f"Ip_information{ip}.txt") as ip_info:
                api_information = os.system(f"curl ipinfo.io/{ip}")
                ip_info.write(api_information)

        case _:
            print("Command currently not found")
            os.system(command)


def main():
    while 1:
        command = input(f"Hello,  {platform.node()}: ")
        main_script(command)
    
if __name__ == "__main__":
    if platform == "linux" or "linux2" or "darwin":
            os.system("clear")
    elif platform == "win32":
        os.system("cls")
    else:
        pass

    words = "Welcome to 1CY-OSINT, the automated OSINT Toolkit for information gathering made easy"
    for char in words:
        sys.stdout.write(char)
        sys.stdout.flush
        sleep(0.050)

    main()