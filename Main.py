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

# Variabili globali per browser e page
browser = None
page = None

async def initialize():
    global browser, page
    # Inizializza il browser e la pagina
    browser = await launch(headless=True)  # Avvia il browser
    page = await browser.newPage()         # Crea una nuova scheda



async def LogIn():
    page.goto('https://www.operatore112.it/users/sign_in')
    page.waitForSelector('user_email')
    page.type('user_email', 'Marco01spino@gmail.com')
    page.waitForSelector('user_password')
    page.type('user_password', 'Gemelli@2001')
    page.click('#submit-button-id')
    print("Sono qui")
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


async def main():
    # Inizializza il browser e la pagina
    await initialize()
    
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


# Esegui il codice asincrono
asyncio.get_event_loop().run_until_complete(main())