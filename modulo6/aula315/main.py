from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    TIME_WAIT = 60

    options = ()

    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com.br/')

    # search_box = WebDriverWait(browser, TIME_WAIT).until(
    #     EC.presence_of_element_located(
    #         (By.ID, 'APjFqb')
    #     )
    # )
    # search_box.send_keys('Hello World')
    # search_box.send_keys(Keys.ENTER)

    # results = browser.find_element(By.ID, 'search')
    # links = results.find_elements(By.TAG_NAME, 'a')
    # links[0].click()

    sleep(TIME_WAIT)
