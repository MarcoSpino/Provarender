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

    async def initialize(self):
        # Inizializza il browser e la pagina
        self.browser = await launch(headless=True)
        self.page = await self.browser.newPage()

    async def fetch_content(self):
        print("Sono qui2")
        self.page.goto('https://www.operatore112.it/users/sign_in')
        self.page.waitForSelector('user_email')
        self.page.type('user_email', 'Marco01spino@gmail.com')
        self.page.waitForSelector('user_password')
        self.page.type('user_password', 'Gemelli@2001')
        self.page.click('#submit-button-id')
        print("Sono qui")
        try:
            # check we are logged in- by grabbing a random tag only visible on log in.
            alliance = self.page.querySelector('#alliance_li')
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

    async def close(self):
        # Chiude il browser
        await self.browser.close()

async def main():
    # Crea un'istanza della classe
    handler = BrowserHandler()
    
    # Inizializza il browser e la pagina
    await handler.initialize()
    
    await handler.fetch_content()
    
    # Chiudi il browser
    await handler.close()

# Esegui il codice asincrono
asyncio.get_event_loop().run_until_complete(main())
