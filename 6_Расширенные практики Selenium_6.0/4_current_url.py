from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get('https://rzd.ru')

url = browser.current_url

print(url)
print(browser.title)

browser.quit()
