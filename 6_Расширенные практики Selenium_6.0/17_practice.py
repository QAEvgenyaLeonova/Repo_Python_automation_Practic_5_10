from faulthandler import is_enabled
from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.by import By #не забудьте импортировать класс By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
browser = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))


#явное ожидание
'''browser.get("http://the-internet.herokuapp.com")

# Явное ожидание: ждать появления элемента с текстом "A/B Testing"
element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "A/B Testing"))
    )
print(f"Элемент {element.text} найден и виден")

browser.quit()'''
###################################################################
#явное ожидание
driver.implicitly_wait(10)
driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

# Найти элемент "Check All" и проверить его наличие
check_all_button = driver.find_element(By.ID, "check1")
check_all_button.click()

print("Элемент 'Check All' найден и кликнут")

driver.quit()














