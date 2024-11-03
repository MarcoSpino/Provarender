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


# Install Pyppeteer
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyppeteer"])

import asyncio
from pyppeteer import launch
import json
import time

# Configuration
username = "Marco01spino@gmail.com"
password = "Gemelli@2001"
BASE_URL = "https://www.operatore112.it/"

class MissonChiefBot:
    def __init__(self):
        self.browser = None
        self.page = None

    async def init_browser(self):
        # Initialize the browser
        self.browser = await launch(headless=True, args=['--no-sandbox'])
        self.page = await self.browser.newPage()
        await self.page.setViewport({"width": 1920, "height": 1080})

    async def login(self):
        await self.page.goto("https://www.operatore112.it/users/sign_in")
        await self.page.type("#user_email", username)
        await self.page.type("#user_password", password)
        await self.page.click('input[name="commit"]')
        await self.page.waitForSelector("#alliance_li", {"timeout": 10000})
        print("Logged in")

    async def get_buildings(self):
        await self.page.goto(BASE_URL + "leitstellenansicht")
        building_links = await self.page.evaluate("""
            () => Array.from(document.querySelectorAll("a[href*='buildings']"))
            .map(el => el.href)
        """)
        print(f"{len(building_links)} edifici trovati")
        # Process building data...
    
    async def get_vehicles(self):
        await self.page.goto(BASE_URL + "vehicles")
        vehicle_links = await self.page.evaluate("""
            () => Array.from(document.querySelectorAll("a[href*='vehicles']"))
            .map(el => el.href)
        """)
        print(f"{len(vehicle_links)} veicoli trovati")
        # Process vehicle data...

    async def fetch_missions(self):
        await self.page.goto(BASE_URL)
        mission_links = await self.page.evaluate("""
            () => Array.from(document.querySelectorAll("#mission_list a:not(.map_position_mover)"))
            .map(el => el.href)
        """)
        print(f"{len(mission_links)} missioni trovate")
        # Process mission data...

    async def dispatch_missions(self):
        # Example of how to navigate and dispatch missions
        for mission_url in self.missionList:
            await self.page.goto(mission_url)
            # Find mission elements and execute required tasks

    async def close(self):
        await self.browser.close()

async def main():
    bot = MissonChiefBot()
    await bot.init_browser()
    await bot.login()
    await bot.get_buildings()
    await bot.get_vehicles()
    await bot.fetch_missions()
    await bot.dispatch_missions()
    await bot.close()

# Run the bot
asyncio.run(main())
