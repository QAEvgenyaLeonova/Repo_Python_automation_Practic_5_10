import re
from time import sleep
from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get('https://www.labirint.ru/')

    def get_counter(self):
        basket = self._driver.find_element(By.CSS_SELECTOR, '.b-header-b-personal-e-link.top-link-main.analytics-click-js.cart-icon-js')
        basket.click()

        sleep(2)

        text_element_book = self._driver.find_element(By.CSS_SELECTOR, '#basket-default-prod-count2').text
        match = re.search(r'\d+', text_element_book)
        if match:
            number_in_text = int(match.group())
        else:
            raise ValueError('Число не найдено в тексте')

        return number_in_text