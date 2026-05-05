from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.edge.service  import  Service  as  EdgeService

edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))
driver.implicitly_wait(20)

driver.get('http://www.uitestingplayground.com/ajax')

driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

content = driver.find_element(By.CSS_SELECTOR, '#content')
txt = content.find_element(By.CSS_SELECTOR, '.bg-success').text
print(txt)

sleep(5)
driver.quit()