from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Inizializza il driver di Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Vai alla pagina desiderata
    driver.get('https://example.com')
    
    # Trova l'elemento <body> e ottieni il suo testo
    body = driver.find_element(By.TAG_NAME, 'body')
    content = body.text
    print("Testo della pagina:\n")
    print(content)
    
    # Chiudi il browser
    driver.quit()

# Esegui il codice
main()
