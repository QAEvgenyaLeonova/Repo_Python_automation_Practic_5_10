from selenium import webdriver

driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.labirint.ru/")

search_field = "#search-field" #мы уже создали переменную со значением локатора
search_input = driver.find_element(By.CSS_SELECTOR, search_field) #помещаем переменную
search_input.send_keys('Python') #отправить значение Python в поисковую строку
search_input.send_keys(Keys.RETURN) #выполнить поиск./ для компактной клавиатуры, как на MacBook
product_card = 'div.product-card'

#собрать все карточки товаров(количество)
books = driver.find_elements(By.CSS_SELECTOR, product_card)
print(len(books))

#for book in books:
#    print(book.text) #Вся информация о книгах

#for book in books: #(находим по автору все 60 книг , но в данной проверке 60 книг но названы втором только 59 книг)
#	author = book.find_element(By.CSS_SELECTOR, '.product-card__author').text
#	print(author)

for book in books:
	title = book.find_element(By.CSS_SELECTOR, '.product-card__name').text
	price = book.find_element(By.CSS_SELECTOR, '.product-card__price-current').text
	author = " "
	try:
		author = book.find_element(By.CSS_SELECTOR, '.product-card__author').text
	except:
		author = "Автор не указан"
	print(author + "\t" + title + "\t" + price)


sleep(3)

























