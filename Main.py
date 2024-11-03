import asyncio
from pyppeteer import launch

import subprocess
import sys
def install():
    subprocess.check_call([sys.executable, "-m", "playwright", "install"])

install()

from colorama import init, Fore, Style
import time
import sys
import os


# Install Pyppeteer
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "playwright", "install"])

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com")
    page.screenshot(path="example.png")
    browser.close()
