# Nightmare was proudly coded by Shade (https://github.com/Shade3421).
# Copyright (c) 2022 Shade#3421 | https://shade.army

import fade, os, requests, shutil, multiprocessing, ctypes
center = shutil.get_terminal_size().columns


P = '\033[35m' # purple
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
RE = '\033[0m' # reset
Y = '\033[33m' # yellow
B = '\033[34m' # blue
LG = '\033[37m' # lightgrey
BP = '\033[1;35m' # bold purple
BR = '\033[1;31m' # bold red
BG = '\033[1;32m' # bold green
BC = '\033[1;36m' # bold cyan
BRE = '\033[1;0m' # bold reset
BY = '\033[1;33m' # bold yellow
BB = '\033[1;34m' # bold blue
BLG = '\033[1;37m' # bold lightgrey
BGP = '\033[7;35m' # background purple
BGRE = '\033[7;0m' # background reset
BGR = '\033[7;31m' # background red
BGG = '\033[7;32m' # background green 
BGC = '\033[7;36m' # background cyan 
BGY = '\033[7;33m' # background yellow 
BGB = '\033[7;34m' # background blue  
BGLG = '\033[7;37m' # background light grey
ULP = '\033[4;35m' # underline purple
ULR = '\033[4;31m' # underline red
ULG = '\033[4;32m' # underline green
ULC = '\033[4;36m' # underline cyan
ULRE = '\033[4;0m' # underline reset
ULY = '\033[4;33m' # underline yellow
ULB = '\033[4;34m' # underline blue
ULLG = '\033[4;37m' # underline lightgrey

ctypes.windll.kernel32.SetConsoleTitleW("Nightmare")

buh = f'''
                          ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
                          ████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
                          ██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
                          ██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
> https://shade.army      ██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
> Creator Shade#3421      ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝



                  [1] MassDM            [2] MassReport            [3] TokenCrasher            [4] WBSpammer
'''

faded_text = fade.purplepink(buh)
print(faded_text)

choice = input(f"{C} >>> {RE}")

if choice == '1':
    os.system("cls")
    import utils.massdm

if choice == '2':
    os.system("cls")
    import utils.reporter

if choice == '3':
    os.system("cls")
    import utils.tokencrasher

if choice == '4':
    os.system("cls")
    import utils.wbspammer