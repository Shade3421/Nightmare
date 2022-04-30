import requests
import json
import os
import threading
import discord
from colorama import init, Fore
import time
import shutil
center = shutil.get_terminal_size().columns

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

class Main:
    def __init__(self):
        self.GUILD_ID = input(f'{gray}[{dblue}?{gray}]{white} Guild ID:{Fore.RESET} ')
        self.CHANNEL_ID = input(f'{gray}[{dblue}?{gray}]{white} Channel ID:{Fore.RESET} ')
        self.MESSAGE_ID = input(f'{gray}[{dblue}?{gray}]{white} Message ID:{Fore.RESET} ')
        REASON = input(
            '\n[1] Illegal content\n'
            '[2] Harassment\n'
            '[3] Spam or phishing links\n'
            '[4] Self-harm\n'
            '[5] NSFW content\n\n'
            '[>] Reason: '
        )

        if REASON.upper() in ('1', 'ILLEGAL CONTENT'):
            self.REASON = 0
        elif REASON.upper() in ('2', 'HARASSMENT'):
            self.REASON = 1
        elif REASON.upper() in ('3', 'SPAM OR PHISHING LINKS'):
            self.REASON = 2
        elif REASON.upper() in ('4', 'SELF-HARM'):
            self.REASON = 3
        elif REASON.upper() in ('5', 'NSFW CONTENT'):
            self.REASON = 4
        else:
            print(f'\n{gray}[{dblue}!{gray}]{white} Reason invalid.')
            os.system(
                'title [Nightmare Reporter] - Restart required &&'
                'pause >NUL &&'
                'title [Nightmare Reporter] - Exiting...'
            )
            time.sleep(3)
            os._exit(0)

        self.RESPONSES = {
            '401: Unauthorized': f'{gray}[{dblue}!{gray}]{white} Invalid Discord token.',
            'Missing Access': f'{gray}[{dblue}!{gray}]{white} Missing access to channel or guild.',
            'You need to verify your account in order to perform this action.': f'{gray}[{dblue}!{gray}]{white} Unverified.'
        }
        self.sent = 0
        self.errors = 0

    def _reporter(self):
        report = requests.post(
            'https://discordapp.com/api/v8/report', json={
                'channel_id': self.CHANNEL_ID,
                'message_id': self.MESSAGE_ID,
                'guild_id': self.GUILD_ID,
                'reason': self.REASON
            }, headers={
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'sv-SE',
                'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
                'Content-Type': 'application/json',
                'Authorization': self.TOKEN
            }
        )
        if (status := report.status_code) == 201:
            self.sent += 1
            print(f'{gray}[{dblue}!{gray}]{white} Reported successfully.')
        elif status in (401, 403):
            self.errors += 1
            print(self.RESPONSES[report.json()['message']])
        else:
            self.errors += 1
            print(f'{gray}[{dblue}!{gray}]{white} Error: Report Unsuccessful')

    def _update_title(self):
        while True:
            os.system(f'title [Nightmare Reporter] - Sent: {self.sent} ^| Errors: {self.errors}')
            time.sleep(0.1)

    def _multi_threading(self):
        threading.Thread(target=self._update_title).start()
        while True:
            if threading.active_count() <= 300:
                threading.Thread(target=self._reporter).start()

    def setup(self):
        recognized = None
        if os.path.exists(config_json := 'Config.json'):
            with open(config_json, 'r') as f:
                try:
                    data = json.load(f)
                    self.TOKEN = data['discordToken']
                except (KeyError, json.decoder.JSONDecodeError):
                    recognized = False
                else:
                    recognized = True
        else:
            recognized = False

        if not recognized:
            self.TOKEN = input(f'{gray}[{dblue}?{gray}]{white} Discord token:{Fore.RESET} ')
            with open(config_json, 'w') as f:
                json.dump({'discordToken': self.TOKEN}, f)
        print()
        self._multi_threading()


if __name__ == '__main__':
    os.system('cls && title [Nightmare Reporter] By Shade#3421 - Main Menu')

buh = '''
  ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
  ████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
  ██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
  ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
Shade#3421
https://shade.army
'''
for line in buh.splitlines():
    print(f'\033[35m {line}'.center(center).replace("█",f"\033[0m█\033[35m"))

border = "\033[0m─"*center
print(border.center(center))

main = Main()
main.setup()
