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


import asyncio
from pyppeteer import launch

class BrowserHandler:
        
    def __init__(self):
        self.browser = None
        self.page = None
        
        self.hrefs = []
        self.missionList = []
        self.vehicleList = []
        self.despatches = []
        self.missionsSeen = []
        self.buildingList = []
        init()



    async def initialize(self):
        # Inizializza il browser e la pagina
        self.browser = await launch(headless=True)
        self.page = await self.browser.newPage()

        

    async def Login(self):
        print("Sono qui2")
        self.page.goto('https://www.operatore112.it/users/sign_in')
        self.page.waitForSelector('user_email')
        self.page.type('user_email', 'Marco01spino@gmail.com')
        self.page.waitForSelector('user_password')
        self.page.type('user_password', 'Gemelli@2001')
        self.page.click('#submit-button-id')
        print("Sono qui")
        try:
            alliance = self.page.querySelector('#alliance_li')
            if alliance:
                class_name = (alliance.getProperty('className')).jsonValue()
                if class_name == "dropdown":
                    print("Logged in")
                    return True
            else:
                return False
        except Exception as e:
            return False
    

async def main():
    # Crea un'istanza della classe
    handler = BrowserHandler()
    
    # Inizializza il browser e la pagina
    await handler.initialize()
    
    logged_in = False
    print(logged_in)
    logged_in = await handler.Login()
    print("RRRRRRRRRRRRRRRR", logged_in)


# Esegui il codice asincrono
asyncio.get_event_loop().run_until_complete(main())