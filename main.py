 # Main file made for running with python3.10
from audioop import reverse
import os
import sys
import platform
from time import sleep
import requests
import random

version = "BETA-V1.10"

def main_script(command: str) -> None:
    match command.split():
        case ["version"]:
            print(f"Version: {version}")

        case ["ip" | "ipinfo", ip]:
            
        

            api_req = requests.get(f"https://ipinfo.io/{ip}")
            with open(f"Ip_information{ip}.txt", "w") as ip_info:
                ip_info.write(api_req.text)

            os.system(f"whois {ip} > whois_{ip}.txt")


            wpscan_ip = os.system(f"wpscan --url http://{ip}/ > wpscan_{ip}.txt")


        case ["help"]:
            print("ip, ipinfo - Get information on an ip")

        case _:
            print("Command currently not found")
            os.system(command)


def main():
    while 1:
        list_greetings = [
            "Hello, ", "Hola, ","Hej, ", "Marhaba, ",
            "Grüß Gott, ", "Namaskar, ","Zdraveite, ",
            "Nǐ hǎo, ","Dobar dan, ","Hallo, ","hyvää päivää, ",
            "Bonjour, ","Guten tag, ","Namaste, ","Shalom, ","Salve, ",
            "Konnichiwa, ","Ahn nyong ha se yo, ","Cześć, ","Olá, ","Sawasdee, ","Merhaba, "]

        random_greeting = random.choice(list_greetings)
        command = input(f"{random_greeting}{platform.node()}: ")
        main_script(command)
    
if __name__ == "__main__":
    if platform == "linux" or "linux2" or "darwin":
            os.system("clear")
    elif platform == "win32":
        os.system("cls")
    else:
        pass

    words = "Welcome to 1CY-OSINT.\n"
    for char in words:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.020)

    main()