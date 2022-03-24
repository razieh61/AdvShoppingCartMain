import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.webdriver.support.ui import Select  # --- add this import for drop down list
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys

s = Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=s)

def setUp():
    print(f'Launch {locators.app} App')
    print(f'-------------------------***--------------------------')
    # make browser full screen
    driver.maximize_window()

    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    # navigate to App website
    driver.get(locators.adshopcart_url)

    # check that URL and the home page title are as expected
    if driver.current_url == locators.adshopcart_url and driver.title == locators.adshopcart_home_page_title:
        print(f'Yey! {locators.app} website launched successfully :)')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)

    else:
        print(f'{locators.app} did not launch. check your code or application')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'-------------------------***--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()  # kill the instance



# setUp()
#
# tearDown()