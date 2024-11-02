import asyncio
from pyppeteer import launch

# Variabili globali per browser e page
browser = None
page = None

async def initialize():
    global browser, page
    # Inizializza il browser e la pagina
    browser = await launch(headless=True)  # Avvia il browser
    page = await browser.newPage()         # Crea una nuova scheda

async def fetch_content():
    # Vai alla pagina desiderata e stampa il contenuto
    await page.goto('https://example.com')
    await page.waitForSelector('body')  # Assicura che il corpo della pagina sia caricato
    content = await page.evaluate('document.body.innerText')
    print("Testo della pagina:\n")
    print(content)

async def main():
    # Inizializza il browser e la pagina
    await initialize()
    # Estrai e stampa il contenuto della pagina
    await fetch_content()
    # Chiudi il browser alla fine
    await browser.close()

# Esegui il codice asincrono
asyncio.get_event_loop().run_until_complete(main())
