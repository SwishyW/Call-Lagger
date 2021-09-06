import os
import time
import threading
from datetime import datetime

os.system(f'cls & mode 85,20 & title Rawr')

import colorama
from colorama import Fore

token = "uwu"
id = input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] {Fore.RESET}ID: {Fore.RESET}")
os.system('cls')

import requests

vc = "https://discord.com/api/v9/channels/"+str(id)+"/call"
msg = "https://discord.com/api/v9/channels/"+str(id)+"/messages"

m = {
    'content': 'Rawr'
}

headers = {
    'Authorization': str(token)
}

requests.post(msg, headers=headers, json=m)

region = [
    'hongkong',
    'europe',
    'brazil',
    'us-central',
    'us-east',
    'sydney',
    'russia',
    'india',
    'japan',
    'us-west',
    'us-south',
    'singapore'
]


import random

def menu():
    now= datetime.now()
    loltime = now.strftime("%H:%M:%S")
    rgc = random.choice(region)
    payload = {
        'region': str(rgc)
    }

    requests.patch(vc, json = payload, headers=headers)
    print(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.MAGENTA}[{Fore.RESET}{loltime}{Fore.MAGENTA}] {Fore.RESET}Region:{Fore.MAGENTA} "+str(rgc))


def console():
  os.system('cls')
  print(f"""{Fore.MAGENTA}╦═╗╔═╗╦ ╦╦═╗
╠╦╝╠═╣║║║╠╦╝
╩╚═╩ ╩╚╩╝╩╚═
[{Fore.RESET}1{Fore.MAGENTA}] {Fore.RESET}Region Spammer
{Fore.MAGENTA}[{Fore.RESET}2{Fore.MAGENTA}] {Fore.RESET}Credits
""")
  choice = input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] {Fore.RESET}Choice: {Fore.MAGENTA}")
  if choice == "1":
    for i in range(999999):
      threading.Thread(target=menu).start()
  if choice == "2":
    os.system('cls')
    print(f"""{Fore.RESET}
      Credits:{Fore.MAGENTA}
╔══════════════════════╗
║{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] {Fore.RESET}Pw{Fore.MAGENTA}                ║
║{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] {Fore.RESET}Heartkill{Fore.MAGENTA}         ║
║{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] {Fore.RESET}Swishy{Fore.MAGENTA}            ║
╚══════════════════════╝
    """)
    time.sleep(3)
    console()
  else:
    print(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] {Fore.RESET}Invalid Choice")
    time.sleep(3)
    console()

if __name__ == "__main__":
    console()
