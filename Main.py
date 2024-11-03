from playwright.sync_api import sync_playwright
import json
import time
from colorama import init, Fore, Style

# Configuration settings
username = "Marco01spino@gmail.com"
password = "Gemelli@2001"
BASE_URL = "https://www.operatore112.it/"

class AlreadyExistsException(Exception):
    pass

class NothingToDespatch(Exception):
    pass

# Initialize Playwright
def initialize_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Switch to False to see the browser
        context = browser.new_context()
        page = context.new_page()
        return page, browser

# Login function using Playwright
def log_in(page):
    page.goto(f"{BASE_URL}users/sign_in")
    page.fill("input#user_email", username)
    page.fill("input#user_password", password)
    page.click("button[name='commit']")
    time.sleep(2)  # Let the page load
    try:
        alliance = page.query_selector("li#alliance_li")
        if alliance and "dropdown" in alliance.get_attribute('class'):
            print("Logged in successfully.")
            return True
        else:
            print("Login failed.")
            return False
    except:
        print("Could not log in.")
        return False

class MissionChiefBot:
    def __init__(self):
        self.hrefs = []
        self.missionList = []
        self.vehicleList = []
        self.buildingList = []
        init()
        
        self.page, self.browser = initialize_browser()
        
        logged_in = log_in(self.page)
        if logged_in:
            self.get_building_list()
            self.get_vehicle_list()
            self.get_staff()
            while True:
                try:
                    self.build_mission_list()
                    self.do_missions()
                    print(Fore.LIGHTBLUE_EX, "Waiting for 5 seconds...")
                    time.sleep(5)
                except Exception as e:
                    print(Fore.RED + "Error occurred, restarting bot..." + Style.RESET_ALL)
                    print(e)
        else:
            print("Login unsuccessful.")
    
    def get_building_list(self):
        hrefs = []
        self.page.goto(BASE_URL + "leitstellenansicht")
        links = self.page.query_selector_all("//a[contains(@href,'buildings')]")
        for link in links:
            hrefs.append(link.get_attribute("href"))
        print(f"{len(links)} buildings found.")
        # Code continues similarly with a loop to extract buildings...

    def get_vehicle_list(self):
        print("Retrieving vehicle list...")
        hrefs = []
        self.page.goto(BASE_URL + "vehicles")
        links = self.page.query_selector_all("//a[contains(@href,'vehicles')]")
        for link in links:
            hrefs.append(link.get_attribute("href"))
        print(f"{len(links)} vehicles found.")
        # Further vehicle list handling code follows...

    def get_staff(self):
        for building in self.buildingList:
            buildingID = building.getID()
            self.page.goto(f"{BASE_URL}buildings/{buildingID}")
            try:
                hire_link = self.page.query_selector(f"//a[contains(@href,'buildings/{buildingID}/hire')]").get_attribute("href")
                self.page.goto(hire_link)
                if self.page.query_selector(f"//a[contains(@href,'buildings/{buildingID}/hire_do/3')]"):
                    self.page.click(f"//a[contains(@href,'buildings/{buildingID}/hire_do/3')]")
                    print(Fore.GREEN, "Started hiring.")
            except:
                print(Fore.YELLOW, "Hiring could not be started.")
    
    def build_mission_list(self):
        self.page.goto(BASE_URL)
        hrefs = []
        self.missionList = []
        links = self.page.query_selector_all("//div[@id='mission_list']//a[not(contains(@class, 'map_position_mover'))]")
        for link in links:
            hrefs.append(link.get_attribute("href"))
        print(f"{len(links)} missions found.")
        # Additional mission list building logic here...

    def do_missions(self):
        print(Fore.MAGENTA + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Missions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + Style.RESET_ALL)
        for mission in self.missionList:
            print(f"Mission: {mission.getName()}")
        # Mission processing logic follows...

# Start the bot
def start_bot():
    MissionChiefBot()

if __name__ == '__main__':
    start_bot()
