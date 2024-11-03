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

class AutoLogin:
    def __init__(self, username, password, login_url):
        self.username = username
        self.password = password
        self.login_url = login_url
        self.browser = None
        self.page = None

    async def start_browser(self):
        """Avvia il browser e apre una nuova pagina."""
        self.browser = await launch(headless=True)  # Imposta headless=False per vedere la finestra del browser
        self.page = await self.browser.newPage()

    async def navigate_to_login(self):
        """Naviga all'URL di login."""
        await self.page.goto(self.login_url)

    async def perform_login(self, username_selector, password_selector, submit_selector):
        """Inserisce le credenziali e invia il form."""
        await self.page.type(username_selector, self.username)  # Campo username
        await self.page.type(password_selector, self.password)  # Campo password
        await self.page.click(submit_selector)  # Pulsante di submit
        await self.page.waitForNavigation()  # Attende che la pagina si carichi dopo il login

    async def main(self, username_selector, password_selector, submit_selector):
        """Esegue le operazioni per il login."""
        await self.start_browser()
        await self.navigate_to_login()
        await self.perform_login(username_selector, password_selector, submit_selector)
        print("Login eseguito con successo!")
        # Qui puoi aggiungere altre operazioni da eseguire dopo il login

    async def close_browser(self):
        """Chiude il browser."""
        await self.browser.close()

# Esempio di utilizzo
async def execute_login():
    # Credenziali e URL
    username = 'Marco01spino@gmail.com'
    password = 'Gemelli@2001'
    login_url = 'https://www.operatore112.it/users/sign_in'

    # Selettori specifici del sito
    username_selector = '#user_email'  # Cambia con il selettore effettivo
    password_selector = '#user_password'  # Cambia con il selettore effettivo
    submit_selector = '#commit'     # Cambia con il selettore effettivo

    # Crea un'istanza di AutoLogin e avvia il processo di login
    auto_login = AutoLogin(username, password, login_url)
    await auto_login.main(username_selector, password_selector, submit_selector)
    await auto_login.close_browser()

# Esegue il codice asincrono
asyncio.get_event_loop().run_until_complete(execute_login())
