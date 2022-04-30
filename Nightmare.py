# Nightmare was proudly coded by Shade (https://github.com/Shade3421).
# Copyright (c) 2022 Shade#3421 | https://shade.army

#######################################################################################

import os
import shutil
import time 
import discord
from tqdm import tqdm
from colorama import Fore, init

center = shutil.get_terminal_size().columns
pcname = (os.getenv('COMPUTERNAME'))

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
dgreen = Fore.GREEN
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTMAGENTA_EX
dblue = Fore.MAGENTA
gray = Fore.LIGHTBLACK_EX
intents = discord.Intents.all()

p1 = '\033[35m' 
g1 = '\033[90m'
w1 = '\033[37m'
P = '\033[35m' # purple
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
RE = '\033[0m' # reset
Y = '\033[33m' # yellow
B = '\033[34m' # blue
LG = '\033[37m' # lightgrey

def start():
    user()


def unlock():
    gui()
    menu()

def exit():
    os._exit(0)


def user():
    os.system("cls")
    print(f"""
                         {C}███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
                         {C}████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
                         {C}██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
                         {C}██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
                         {C}██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
                         {C}╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
    """)
    username = input(f"""
{C}╔═[{pcname}@Nightmare]
{C}╚══[{p1}USERNAME{C}]═>{RE} """)
    if username == "Nightmare" or username == "nightmare":
        print(f"{G}Correct!")
        time.sleep(1.5)
        pw()
    else:
        print(f"{R}Incorrect!")
        time.sleep(1.5)
        user()


def pw():
    os.system("cls")
    print(f"""
                         {C}███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
                         {C}████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
                         {C}██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
                         {C}██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
                         {C}██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
                         {C}╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
    """)
    password = input(f"""
{C}╔═[{pcname}@Nightmare]
{C}╚══[{p1}PASSWORD{C}]═>{RE} """)
    if password == "Root" or password == "root":
        print(f"{G}Correct!")
        time.sleep(1.5)
        unlock()
    else:
        print(f"{R}Incorrect!")
        time.sleep(1.5)
        pw()



def massDM():
    os.system("cls")
    import utils.massdm   

def wb():
    os.system("cls")
    import utils.wbspammer

def reporter():
    os.system("cls")
    import utils.reporter

def tokencrasher():
    os.system("cls")
    import utils.tokencrasher

def teddy():
    os.system("cls")
    import utils.teddybuilder


def gui():
    os.system('cls & title Nightmare : Made By Shade#3421')
    print(f"""
                         {C}███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
                         {C}████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
                         {C}██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
                         {C}██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
{R}> https://shade.army     {C}██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
{R}> Creator Shade#3421     {C}╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

                                       {p1}──────────────────────────────────────────{w1}
                                        {p1}────────────────────────────────────────{w1}
                                         {p1}╔══════════════════╦═════════════════╗{w1}
                                         {p1}║ {w1}[{p1}1{w1}] TokenCrash   {p1}║ {w1}[{p1}2{w1}] Teddy       {p1}║{w1}
                                         {p1}║ {w1}[{p1}3{w1}] WBSpammer    {p1}║ {w1}[{p1}4{w1}] MassReport  {p1}║{w1}
                                         {p1}║ {w1}[{p1}5{w1}] MassDM       {p1}║ {w1}[{p1}6{w1}] soon        {p1}║{w1}
                                         {p1}╚══════════════════╩═════════════════╝{w1} 
""")

def menu():
    x = input(f"""
{C}╔═[{pcname}@Nightmare]
{C}╚══[{p1}OPTION{C}]═>{RE} """)
    if x == '1':
        tokencrasher()
    else:
        unlock()

    if x == '2':
        teddy()
    else:
        unlock()
        
    if x == '3':
       wb()
    else:
        unlock()
               
    if x == '4':
      reporter()
    else:
        unlock() 
    if x == '5':
       massDM()
    else:
        unlock()

    if x == '6':
        print(f"{R}Not Released Yet{RE}")
        unlock()
    else:
        unlock()

if __name__ == "__main__":  
    os.system("title Loading Nightmare...")
    progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    for item in progressbar:
        time.sleep(0.1)
    progressbar.set_description(' Loading Nightmare: ')

time.sleep(3)
print("\n")

progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33])
for item in progressbar:
        time.sleep(0.1)
progressbar.set_description(' Loading utils: ')
start()