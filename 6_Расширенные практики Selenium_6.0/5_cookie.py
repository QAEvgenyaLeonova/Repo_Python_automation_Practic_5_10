from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

my_cookie = {
	'name': 'cookie_policy',
	'value': '1'}

driver.get("https://labirint.ru/")
driver.add_cookie(my_cookie)

my_cookie = driver.get_cookies('expiry')
print(my_cookie)

cookie = driver.get_cookie('PHPSESSID') #положили метод в переменную cookie
print(cookie) #запрос на вывод данных в терминал

#driver.refresh()
#driver.delete_all_cookies()

driver.refresh()

sleep(10)
driver.quit()