import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get('https://rzd.ru')

current_title = browser.title

print(current_title)

time.sleep(10)
browser.quit()