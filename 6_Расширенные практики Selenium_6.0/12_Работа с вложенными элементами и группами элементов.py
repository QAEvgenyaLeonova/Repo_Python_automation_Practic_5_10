from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.edge.service  import  Service  as  EdgeService

edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))

driver.get("https://the-internet.herokuapp.com/checkboxes")

#ИЩЕМ ЭЛЕМЕНТЫ
divs = driver.find_elements(By.CSS_SELECTOR, 'div')
l = len(divs)
print(divs)

driver.quit()