import asyncio
from pyppeteer import launch

import subprocess
import sys
def install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])

install()

from colorama import init, Fore, Style
import time
import sys
import os



async def main():
    global browser, page
    browser = await launch(headless=True)
    page = await browser.newPage()

main()

class MissonChiefBot:
    def __init__(self):
        self.hrefs = []
        self.missionList = []
        self.vehicleList = []
        self.despatches = []
        self.missionsSeen = []
        self.buildingList = []
        init()
        logged_in = LogIn()
        if logged_in:
            self.edificiList()
            self.veicoliList()
            self.personale()
            while True:
                try:
                    print(Fore.LIGHTBLUE_EX, "Aspetto 5 secondi")
                    time.sleep(5)
                except Exception as e:
                    print(Fore.RED + "Oh no, an error occurred." + Style.RESET_ALL)
                    print(e)
                    print(Fore.RED + "Restarting bot...." + Style.RESET_ALL)
        else:
            print("Couldn't log in...")


# OK NON TOCCARE
def LogIn():
    page.goto('https://www.operatore112.it/users/sign_in')
    page.waitForSelector('user_email')
    page.type('user_email', 'Marco01spino@gmail.com')
    page.waitForSelector('user_password')
    page.type('user_password', 'Gemelli@2001')
    page.click('#submit-button-id')
    try:
        # check we are logged in- by grabbing a random tag only visible on log in.
        alliance = page.querySelector('#alliance_li')
        if alliance:
            # Ottieni il valore dell'attributo 'class'
            class_name = (alliance.getProperty('className')).jsonValue()
        
            # Controlla se la classe è uguale a "dropdown"
            if class_name == "dropdown":
                print("Logged in")
                return True
        else:
            return False
    except Exception as e:
        return False

def begin():
    MissonChiefBot()


if __name__ == '__main__':
    try:
        begin()
    except KeyboardInterrupt:
        print('Closing..')
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)
