from selenium.webdriver.support.ui import WebDriverWait
from locator_store import Store

class AddToCart:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def add_backpack_basket(self):
        self.driver.find_element(*Store.ADD_BACKPACK_BASKET).click()

    def add_shirt_basket(self):
        self.driver.find_element(*Store.ADD_SHIRT_BASKET).click()

    def add_onesie_basket(self):
        self.driver.find_element(*Store.ADD_ONESIE_BASKET).click()

    def button_basket_click(self):
        self.driver.find_element(*Store.BASKET).click()

    def expectation(self):
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

