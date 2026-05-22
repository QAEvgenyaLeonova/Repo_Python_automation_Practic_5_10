from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        # Локатор поля поиска
        self.search_input = (By.NAME, 'q')
        # Локатор результатов поиска
        self.results = (By.CSS_SELECTOR, 'div.g')

    def open(self):
        self.driver.get('https://www.google.com/')


    def input_search_query(self, search_query):
        try:
            search_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.search_input)
            )
            search_field.clear()
            search_field.send_keys(search_query)
            search_field.send_keys(Keys.RETURN)
        except TimeoutException:
            print("Не удалось найти поле поиска")
            return False
        return True

    def get_search_results(self):
        try:
            results = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.results)
            )
            return results
        except TimeoutException:
            print("Не удалось найти результаты поиска")
            return []