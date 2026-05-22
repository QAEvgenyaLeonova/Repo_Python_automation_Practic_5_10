from locator_store import Store
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MakingStore:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_name(self, name):
        self.wait.until(EC.presence_of_element_located(Store.FIRST_NAME)).send_keys(name)

    def fill_last_name(self, surname):
        self.wait.until(EC.presence_of_element_located(Store.LAST_NAME)).send_keys(surname)

    def fill_postal_code(self, code):
        self.wait.until(EC.presence_of_element_located(Store.INDEX_COD)).send_keys(code)

    def click_continue(self):
        self.driver.find_element(*Store.BUTTON_CONTINUE).click()

    def get_count_total(self):
        total_element = self.wait.until(EC.presence_of_element_located(Store.TOTAL_ELEMENT))
        total_text = total_element.text
        total_value = total_text.replace('Total: ', '').strip()
        return total_value

    def finish_button(self):
        self.driver.find_element(*Store.BUTTON_FINISH).click()

    def back_to_store(self):
        self.driver.find_element(*Store.BUTTON_BACK).click()

