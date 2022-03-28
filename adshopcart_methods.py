import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.webdriver.support.ui import Select


s = Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app} App')
    print(f'-------------------------***--------------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.adshopcart_url)
    if driver.current_url == locators.adshopcart_url and driver.title == locators.adshopcart_home_page_title:
        print(f'Yey! {locators.app} website launched successfully :)')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. check your code or application')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')


def tearDown():
    if driver is not None:
        print(f'-------------------------***--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


def sign_up():
    print(f'------------------------ sign_up -------------------------')
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(0.25)
    assert driver.find_element(By.CLASS_NAME, 'PopUp').is_displayed()
    sleep(2)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(0.5)
    assert driver.current_url == locators.adshopcart_signup_page_url
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//h3[contains(.,"CREATE ACCOUNT")]')
    sleep(0.5)
    driver.find_element(By.XPATH, '//input[@name="usernameRegisterPage"]').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="emailRegisterPage"]').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="passwordRegisterPage"]').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="confirm_passwordRegisterPage"]').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="first_nameRegisterPage"]').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="last_nameRegisterPage"]').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="phone_numberRegisterPage"]').send_keys(locators.phonenum)
    sleep(0.25)
    Select(driver.find_element(By.XPATH, '//select[@name="countryListboxRegisterPage"]')).select_by_visible_text(locators.country)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="cityRegisterPage"]').send_keys(locators.city)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="addressRegisterPage"]').send_keys(locators.address)
    sleep(0.5)
    driver.find_element(By.XPATH, '//input[@name="state_/_province_/_regionRegisterPage"]').send_keys(locators.state)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name = "postal_codeRegisterPage"]').send_keys(locators.postal_code)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name = "i_agree"]').click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//button[@id = "register_btnundefined"]').is_enabled()
    sleep(0.5)
    driver.find_element(By.XPATH, '//button[@id = "register_btnundefined"]').click()
    sleep(0.25)
    print(f' New user {locators.new_username}/{locators.new_password}/{locators.email} is added successfully')


def check_full_name():
    print(f'------------------------ check_full_name -------------------------')
    assert driver.current_url == locators.adshopcart_url
    sleep(1)
    driver.find_element(By.ID, "menuUserLink").click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@id = "loginMiniTitle"]//label[contains(., "My account")]').click()
    sleep(3)
    if driver.current_url == locators.adshopcart_myaccount_url:
        sleep(1)
        if driver.find_element(By.XPATH, f'//label[contains(text(), "{locators.full_name}")]').is_displayed():
            sleep(2)
            print(f'--- {locators.full_name} is displayed in MY ACCOUNT page')
        else:
            sleep(0.5)
            print(f'--- {locators.full_name} is not displayed in MY ACCOUNT page')
    else:
        print('you are not in MY ACCOUNT page!')


def check_orders():
    print(f'------------------------ check_orders -------------------------')
    driver.find_element(By.ID, "menuUserLink").click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@id = "loginMiniTitle"]//label[contains(., "My orders")]').click()
    sleep(0.5)
    assert driver.current_url == locators.adshopcart_myorders_url
    sleep(1)
    if driver.find_element(By.XPATH,'//label[contains(text(), " - No orders - ")]').is_displayed():
        sleep(0.5)
        print(f'--- no order from {locators.full_name}')
    else:
        sleep(0.5)
        print(f' {locators.full_name} has orders')


def log_out():
    print(f'------------------------ log_out -------------------------')
    sleep(0.5)
    driver.find_element(By.ID, "menuUserLink").click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@id = "loginMiniTitle"]//label[contains(., "Sign out")]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//span[contains(@class,"containMiniTitle")]').text == '':
        sleep(0.5)
        print(f' user {locators.new_username} is signed out successfully')
    else:
        sleep(0.5)
        print(f' user {locators.new_username} is not signed out successfully')
    sleep(2)


def log_in(username, password):
    print(f'------------------------ log_in -------------------------')
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(1)
    assert driver.find_element(By.XPATH, '//login-modal//div[@class="PopUp"]').is_displayed()
    # assert driver.find_element(By.CLASS_NAME, 'PopUp').is_displayed()
    sleep(3)
    driver.find_element(By.XPATH, '//input[@name = "username"]').send_keys(username)
    sleep(0.5)
    driver.find_element(By.XPATH, '//input[@name = "password"]').send_keys(password)
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//button[@id = "sign_in_btnundefined"]').is_enabled()
    sleep(0.5)
    driver.find_element(By.XPATH, '//button[@id = "sign_in_btnundefined"]').click()
    sleep(0.5)
    if driver.find_element(By.XPATH, '//label[@id = "signInResultMessage"]').text == 'Incorrect user name or password.':
        print('Invalid username and password has entered, user does not exist!!')
        sleep(0.5)
    else:
        sleep(0.5)
        if driver.find_element(By.XPATH, '//span[contains(@class,"containMiniTitle")]').text == username:
            print(f' user {username} is signed in successfully')
        else:
            print(f' user {username} is not signed in successfully')
        sleep(0.25)


def delete_test_account():
    print(f'------------------------ delete_test_account -------------------------')
    assert driver.current_url == locators.adshopcart_url
    sleep(0.5)
    driver.find_element(By.ID, "menuUserLink").click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@id = "loginMiniTitle"]//label[contains(., "My account")]').click()
    sleep(0.5)
    if driver.current_url == locators.adshopcart_myaccount_url:
        sleep(2)
        driver.find_element(By.XPATH, '//button[contains(@class,"deleteMainBtnContainer")]').click()
        sleep(2)
        if driver.find_element(By.XPATH, '//div[@id="deleteAccountPopup"]').is_displayed():
            sleep(3)
            test = driver.find_element(By.XPATH, '//div[contains(text(),"yes")]')
            test.click()
            sleep(5)
            if driver.find_element(By.XPATH, '//span[contains(@class,"containMiniTitle")]').text == '':
                print(f' user {locators.new_username} is deleted successfully')
            else:
                print(f' user {locators.new_username} is not deleted successfully')
        else:
            sleep(1)
            print('The deleteAccountPopup is not displayed')
    else:
        print('you are not in MY ACCOUNT page!')
    sleep(0.25)
