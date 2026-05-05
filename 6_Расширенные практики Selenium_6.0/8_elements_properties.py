from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.edge.service  import  Service  as  EdgeService

edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))


txt = driver.find_element(By.CSS_SELECTOR, 'a[href*="text=USD"]').text
print(txt)

tag = driver.find_element(By.CSS_SELECTOR, 'a[href*="text=USD"]').tag_name
print(tag)

id_el = driver.find_element(By.CSS_SELECTOR, 'a[href*="text=USD"]').id
print(id_el)

attrib_href = driver.find_element(By.CSS_SELECTOR, 'a[href*="text=USD"]').get_attribute('href')
print(attrib_href)

font_family = driver.find_element(By.CSS_SELECTOR, 'a[href*="text=USD"]').value_of_css_property('font-family')
print(font_family)

font_color = driver.find_element(By.CSS_SELECTOR, 'a[href*="text=USD"]').value_of_css_property('color')
print(font_color)

sleep(10)

driver.quit()

