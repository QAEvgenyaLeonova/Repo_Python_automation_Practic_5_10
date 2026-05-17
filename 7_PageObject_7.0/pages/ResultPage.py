from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)  # создаем экземпляр WebDriverWait

    def add_books(self):
        all_button_basket = self._driver.find_elements(By.CSS_SELECTOR, '.btn-tocart.buy-link')
        counter = 0
        for btn in all_button_basket:
            btn.click()
            counter += 1
            sleep(1)
        try:
            self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.popup-window-content.b-basket-popinfo')))
            self._driver.execute_script(
                "document.querySelector('.popup-window-content.b-basket-popinfo').style.display='none';")
        except:
            pass
        return counter

    def get_empty_result_message(self):
        divs = self._driver.find_elements(By.CSS_SELECTOR, '.index-top-title-outer')
        for div in divs:
            h1_elements = div.find_elements(By.TAG_NAME, 'h1')
            if h1_elements:
                return h1_elements[0].text
        return ""  # или сообщение, если элементов нет