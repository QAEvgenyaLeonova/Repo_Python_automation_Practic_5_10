import time
from selenium import webdriver
#Импортируем для Edge
from  selenium.webdriver.edge.service  import  Service  as  EdgeService


edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
browser = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))
browser.get('https://ya.ru')

browser.maximize_window()
browser.minimize_window()
browser.fullscreen_window()
browser.set_window_size(1000, 500)
time.sleep(5)


browser.quit()


