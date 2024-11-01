import asyncio
from pyppeteer import launch

async def main():
    # Avvia il browser
    browser = await launch(headless=True)  # headless=True per eseguire senza interfaccia grafica
    page = await browser.newPage()
    
    # Vai alla pagina desiderata
    await page.goto('https://example.com')
    
    # Attendi che la pagina sia caricata completamente
    await page.waitForSelector('body')  # Assicura che il corpo della pagina sia caricato
    
    # Estrai il testo del corpo della pagina
    content = await page.evaluate('document.body.innerText')
    print("Testo della pagina:\n")
    print(content)
    
    # Chiudi il browser
    await browser.close()

# Esegui il codice asincrono
asyncio.get_event_loop().run_until_complete(main())
