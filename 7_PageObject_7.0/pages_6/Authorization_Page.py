from selenium.webdriver.support.ui import WebDriverWait
from locator_store import Store

class AuthorizationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open_driver(self):
        self.driver.get('https://www.saucedemo.com/')

    def enter_username(self, username):
        self.driver.find_element(*Store.INPUT_NAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*Store.INPUT_PASS).send_keys(password)

    def button_click_login(self):
        self.driver.find_element(*Store.BUTTON_LOGIN).click()

    def expectation(self):
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

