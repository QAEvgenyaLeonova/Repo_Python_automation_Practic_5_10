from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By #не забудьте импортировать класс By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru") #переход на сайт

element = driver.find_element(By.CSS_SELECTOR, "#text") #поиск элемента
element.send_keys('test skypro')
element.send_keys(Keys.RETURN)

sleep(10)

driver.quit()

#print(element) #отображение результата в терминале
#element.clear()
#element.click()
#(session="96b434ad3b114f3650cdca8e836b2c47", element="f.9CA4593E8500FE5DAEE76BE44FA9D6D7.d.B8A82C0B1D50CA813E6332F8A85C2051.e.21")