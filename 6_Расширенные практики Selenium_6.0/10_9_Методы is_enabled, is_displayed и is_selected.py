from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.edge.service  import  Service  as  EdgeService

edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))

#РАДИОКНОПКА
'''driver.get('https://demoqa.com/radio-button')

is_enabled = driver.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
print(is_enabled)

not_is_enabled = driver.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
print(not_is_enabled)

sleep(1)

driver.quit()'''


#ЧЕКБОКС
driver.get('https://demoqa.com/checkbox')

cb = driver.find_element(By.CSS_SELECTOR, '[aria-label="Select Home"]')
is_selected = cb.is_selected()
print(is_selected)
sleep(5)

cb.click()

is_selected = cb.is_selected()

print(is_selected)

sleep(5)

driver.quit()


