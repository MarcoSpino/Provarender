import asyncio
from pyppeteer import launch

def main():
    # Definizione della funzione asincrona principale
    async def run():
        # Avvia il browser
        browser = await launch(headless=True)  # Usa headless=False per vedere il browser in azione
        page = await browser.newPage()
        
        # Vai alla pagina desiderata
        await page.goto('https://example.com')
        
        # Attendi che la pagina sia caricata completamente
        await page.waitForSelector('body')
        
        # Estrai il testo del corpo della pagina
        content = await page.evaluate('document.body.innerText')
        print("Testo della pagina:\n")
        print(content)
        
        # Chiudi il browser
        await browser.close()
    
    # Esegui la funzione asincrona principale
    asyncio.run(run())

# Esegui il codice
main()
