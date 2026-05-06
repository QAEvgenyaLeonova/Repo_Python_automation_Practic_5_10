from time import sleep
from selenium import webdriver
#две строки ниже можно оставить, они не помешают работе
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#три строки ниже - новые, импорт драйвера для Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
#Импортируем для Edge
from  selenium.webdriver.edge.service  import  Service  as  EdgeService
from  webdriver_manager.microsoft  import  EdgeChromiumDriverManager

#browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
browser = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))


browser.maximize_window()  # для разворачивания окна
browser.get("https://ya.ru/")  # для перехода на нужную страницу
sleep(5)  # для паузы на загрузку контента страницы

browser.save_screenshot('./ya.png' + browser.name + 'png')  # для сохранения скриншота
browser.quit()  # для закрытия окна





















