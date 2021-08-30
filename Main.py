import os, random, string
import pyperclip as pc
from colorama import Fore

def IsThisTheFirstTime():
    homedir = os.path.expanduser("~")
    if os.path.isfile(f"{homedir}\\pass.txt") == True:
        return False
    else:
        f = open(f"{homedir}\\pass.txt", "w")
        f.close()

IsThisTheFirstTime()

rootDir = os.getenv('USERPROFILE')
os.system('cls')

Logo = f"""
{Fore.YELLOW}╔═╗╔═╗╔═╗╔═╗╦ ╦╔═╗╦═╗╔╦╗  {Fore.WHITE}╔╦╗╔═╗╔╗╔╔═╗╔═╗╔═╗╦═╗
{Fore.YELLOW}╠═╝╠═╣╚═╗╚═╗║║║║ ║╠╦╝ ║║  {Fore.WHITE}║║║╠═╣║║║╠═╣║ ╦║╣ ╠╦╝
{Fore.YELLOW}╩  ╩ ╩╚═╝╚═╝╚╩╝╚═╝╩╚══╩╝  {Fore.WHITE}╩ ╩╩ ╩╝╚╝╩ ╩╚═╝╚═╝╩╚═
"""

Box = f"""
{Fore.YELLOW}╔══════════════════════╗
{Fore.YELLOW}║ {Fore.WHITE}1 {Fore.YELLOW}= {Fore.WHITE}Create Password  {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.WHITE}2 {Fore.YELLOW}= {Fore.WHITE}Show Passwords   {Fore.YELLOW}║
{Fore.YELLOW}║ {Fore.WHITE}3 {Fore.YELLOW}= {Fore.WHITE}Exit             {Fore.YELLOW}║
{Fore.YELLOW}╚══════════════════════╝
"""

def Main():
    os.system('cls')
    print(Logo)
    print(Box)
    choice = input('> ')
    if choice == '1':
        print(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] Website{Fore.YELLOW}:{Fore.WHITE}")
        website = input('> ')
        print(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] Email{Fore.YELLOW}:{Fore.WHITE}")
        email = input('> ')
        print(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] Username{Fore.YELLOW}:{Fore.WHITE}")
        username = input('> ')
        x = 0
        Types = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()"
        Chars = ''
        while x < 16:
            Type = random.choice(Types)
            Chars += random.choice(Type)
            x += 1
        pc.copy(Chars)
        print(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] Password Copied To Clipboard{Fore.YELLOW}!")
        print(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] Password{Fore.YELLOW}:{Fore.WHITE} {Chars}")
        f = open(f"{rootDir}\\pass.txt", "a")
        info = f"""
    \n
    {Fore.YELLOW}============================
    {Fore.WHITE}Website  {Fore.YELLOW}: {Fore.WHITE}{website}
    {Fore.WHITE}Email    {Fore.YELLOW}: {Fore.WHITE}{email}
    {Fore.WHITE}Username {Fore.YELLOW}: {Fore.WHITE}{username}
    {Fore.WHITE}Password {Fore.YELLOW}: {Fore.WHITE}{Chars}
    {Fore.YELLOW}============================
    """
        f.write(info)
        f.close()
        a = input('')
        Main()
    if choice == '2':
        with open(f"{rootDir}\\pass.txt", "r+") as passwords:
            for line in passwords:
                line = line.strip("\n")
                print(line)
        a = input('')
        Main()
    else:
        print(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] Password{Fore.YELLOW}:{Fore.WHITE} Error")
        a = input('')
        Main()
Main()