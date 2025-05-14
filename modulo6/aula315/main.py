from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=CHROMEDRIVER)
    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )
    return chrome_browser

if __name__ == '__main__':
    options = ()
    browser = make_chrome_browser(*options)
    browser.get('https://www.google.com.br/')
    sleep(30)