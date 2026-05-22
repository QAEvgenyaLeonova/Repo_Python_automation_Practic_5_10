from selenium.webdriver.support.ui import WebDriverWait
from locator_store import Store

class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def button_checkout_click(self):
        self.driver.find_element(*Store.BUTTON_CHECKOUT).click()

    def expectation(self):
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')



