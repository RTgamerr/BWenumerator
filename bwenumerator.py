import requests
from colorama import Fore

print("""
 ▄▄▄▄    █     █░▓█████  ███▄    █  █    ██  ███▄ ▄███▓▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▓█████▄ ▓█░ █ ░█░▓█   ▀  ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██▒ ▄██▒█░ █ ░█ ▒███   ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██░█▀  ░█░ █ ░█ ▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▓█  ▀█▓░░██▒██▓ ░▒████▒▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░▒▓███▀▒░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
▒░▒   ░   ▒ ░ ░   ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
 ░    ░   ░   ░     ░      ░   ░ ░  ░░░ ░ ░ ░      ░      ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
 ░          ░       ░  ░         ░    ░            ░      ░  ░   ░           ░  ░            ░ ░     ░     
      ░                                                                                                    
                       01101101 01100001 01100100 01100101  01100010 01111001        
                       01110010 01110100 01100111 00111000 00110011 00111000 00110111                                   

""")
website = input("")
try:
   sub_domains = open("wordlist2-1626415171030.txt").readlines()
except FileNotFoundError:
   print("[-] Wordlist was not found!")
for i in sub_domains:
    request_sent = requests.get(f"{website}/{i}")
    if request_sent == 404 or "not found":
        print(Fore.RED + f"[-] {i} Sub domain not found in {website}" + Fore.RESET)
        print(Fore.RESET)
    else:
        print(Fore.GREEN + f"[+] Sub domain was found in {website}" + Fore.RESET)
        print(Fore.RESET)
    