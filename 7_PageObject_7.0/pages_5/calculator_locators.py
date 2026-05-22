from selenium.webdriver.common.by import By

class CalcLocatorsPage:
    DELAY_FIELD = (By.CSS_SELECTOR, '#delay')#задержка
    INPUT_FIELD = (By.CSS_SELECTOR, 'input[value="5"]')
    BUTTON_SEVEN = (By.XPATH, '//*[@id="calculator"]/div[2]/span[1]')
    BUTTON_PLUS = (By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')
    BUTTON_EIGHT = (By.XPATH, '//*[@id="calculator"]/div[2]/span[2]')
    BUTTON_EQUALLY = (By.XPATH, '//*[@id="calculator"]/div[2]/span[15]')
    RESULT_FIELD = (By.CSS_SELECTOR, '.screen')

