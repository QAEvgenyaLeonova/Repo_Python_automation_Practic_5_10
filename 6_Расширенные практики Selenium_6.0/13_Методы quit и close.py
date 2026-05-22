from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.edge.service  import  Service  as  EdgeService

edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))

driver.get('https://demoqa.com/browser-windows')

driver.find_element(By.CSS_SELECTOR, '#tabButton').click()
sleep(5)

driver.close()

driver.quit(30)