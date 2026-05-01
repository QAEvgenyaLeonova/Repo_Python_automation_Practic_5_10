from selenium import webdriver

driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/") #браузер откроет страницу
driver.get("https://vk.com/") #перейдет на следующую страницу
driver.set_window_size(640, 460) #окно браузера уменьшится под параметры
#driver.maximize_window #открыть окно по размеру экрана
#driver.minimize_window #свернуть окно браузера
#driver.fullscreen_window #развернуть окно на весь экран, аналог F11
#driver.back() #назад
#driver.forward() #Вперед
#driver.refresh() #Обновить


sleep(3)

driver.save_screenshot('./ya.png')























