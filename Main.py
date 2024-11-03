
import subprocess
import sys
def install():
    subprocess.check_call([sys.executable, "-m", "playwright", "install"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])

install()

from playwright.sync_api import sync_playwright

# Avvia Playwright
with sync_playwright() as p:
    # Lancia il browser (in modalità headless)
    browser = p.chromium.launch(headless=True)
    
    # Apre una nuova pagina
    page = browser.new_page()
    
    # Visita example.com
    page.goto("https://example.com")
    
    # Prende il titolo della pagina
    titolo = page.title()
    
    # Stampa il titolo della pagina
    print("Titolo della pagina:", titolo)
    
    # Chiude il browser
    browser.close()

