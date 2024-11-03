import asyncio
from pyppeteer import launch

class MyScraper:
    def __init__(self):
        self.browser = None
        self.page = None

    async def start_browser(self):
        # Avvia il browser
        self.browser = await launch(headless=True)  # headless=False per vedere il browser
        self.page = await self.browser.newPage()
    
    async def go_to_page(self, url):
        # Vai alla pagina specificata
        if self.page:
            await self.page.goto(url)
        else:
            print("Browser non avviato. Chiama start_browser prima di usare questa funzione.")
    
    async def get_content(self, selector):
        # Ottieni il contenuto di un elemento usando un selettore
        if self.page:
            element = await self.page.querySelector(selector)
            if element:
                return await self.page.evaluate('(element) => element.textContent', element)
            else:
                print(f"Elemento {selector} non trovato.")
                return None
        else:
            print("Pagina non caricata.")
            return None

    async def close_browser(self):
        # Chiudi il browser
        if self.browser:
            await self.browser.close()
    
    async def scrape(self, url, selector):
        # Metodo principale per gestire l'intero flusso
        await self.start_browser()
        await self.go_to_page(url)
        content = await self.get_content(selector)
        await self.close_browser()
        return content

# Esecuzione dell'oggetto e della funzione principale
async def main():
    scraper = MyScraper()
    url = "https://example.com"
    selector = "h1"
    content = await scraper.scrape(url, selector)
    print("Contenuto dell'elemento:", content)

# Avvia l'evento asincrono
asyncio.run(main())
