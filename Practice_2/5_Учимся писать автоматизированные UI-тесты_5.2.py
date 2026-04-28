from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

#Заити в лабиринт
driver.get("https://www.labirint.ru/")



#Наити книги по слову Python
search_locator = '#search-field'

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys('Python')
search_input.send_keys(Keys.RETURN)
#2.Способ через зяпятую: search_input.send_keys('Python', Keys.RETURN)


#Собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, 'div.product-card, document')
print(len(books))


#Вывести в консоль инфу : название + аквтор + цена
for book in books:
    title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text
    price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text
    author = ''
try: #Python сам попробует определить значение
    author = book.find_element(By.CSS_SELECTOR, 'div.product-card__author').text
except: #если не получится, то значение мы задали сами
    author = 'Автор не указан'

print(author + '\t' + title + '\t' + price)



#product-card__author

sleep(5)
































