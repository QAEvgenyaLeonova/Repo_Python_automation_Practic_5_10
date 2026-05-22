from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculator_locators import CalcLocatorsPage

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open_driver(self):
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    def set_delay(self, delay):
        self.driver.find_element(*CalcLocatorsPage.DELAY_FIELD).clear()
        self.driver.find_element(*CalcLocatorsPage.DELAY_FIELD).send_keys(delay)

    def click_buttun(self, button_locator):
        self.wait.until(EC.element_to_be_clickable(button_locator)).click()

    def get_result(self):
        result_element_field = self.wait.until(EC.presence_of_element_located(CalcLocatorsPage.RESULT_FIELD))
        self.wait.until(EC.text_to_be_present_in_element(CalcLocatorsPage.RESULT_FIELD, '15'))
        return result_element_field.text

