 # Main file made for running with python3.10
import os
import sys
import platform
from time import sleep
import requests
import random
import phonenumbers
from phonenumbers import carrier,geocoder,timezone


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
            os.system(f"wpscan --url http://{ip}/ > wpscan_{ip}.txt")
            print("Running dnsmap, this can take a while")
            os.system(f"dnsmap {ip}")
            os.system(f"dnsmap {ip} > dnsmap_{ip}.txt")
            os.system(f"dig {ip} > dig_{ip}.txt")
            os.system(f"dig -x {ip} +noall +answer > dig_noall_answer_{ip}.txt")
            os.system(f"whatweb {ip} > whatweb_{ip}.txt")
            os.system(f"certgraph {ip} -details -json -verbose -dns -ct-subdomains > certgraph_{ip}.txt")
            os.system(f"atk6-dnsdict6 -D {ip} > atk6-dnsdict6_{ip}.txt")
            print("Unicornscan in progress, this can take a while")
            os.system(f"unicornscan {ip} > unicornscan_{ip}.txt")
            print("Fast sslscan in progreess, this can still take some time")
            os.system(f"sslscan {ip} > sslscan_{ip}.txt")
            os.system(f"lbd {ip} > lbd_{ip}.txt")

        case ["name" | "username"]:
            print("Starting name / Username scan")
            os.system("python3 Google_search.py")

            sherlock_name_input = input("Name for sherlock: ")
            with open(f"sherlock_{sherlock_name_input}_.txt", "w") as sherlock_name:
                sherlock_search = os.system(f"sherlock {sherlock_name_input}")
                sherlock_name.write(str(sherlock_search))


        case ["phonenumber" | "ph" | "phone"]:
            Num = input("Phone Number: ")
            Num = phonenumbers.parse(Num)

            carrier_Num = carrier.name_for_number(Num, "en")
            geocoder_num = geocoder.description_for_number(Num, "en")
            Validity_Num = "Valid Number: ", phonenumbers.is_valid_number(Num)

            with open(f"PhoneNum_{Num}_Details.txt", "w") as NumDetails:
                NumDetails.write(str(carrier_Num) + "\n")
                NumDetails.write(str(geocoder_num)+ "\n")
                NumDetails.write(str(Validity_Num)+ "\n")



        case ["help"]:
            print("""
ip, ipinfo - Get information on an ip
name, username - Get information on someone from their name or username
phone, phonenumber - Get basic informatino in an iphone num
""")

        case _:
            print("Command currently not found")
            os.system(command)


def main():
    print()
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
