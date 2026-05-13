from faulthandler import is_enabled
from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.by import By #не забудьте импортировать класс By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
#browser = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))

'''browser.maximize_window()
browser.get('https://ya.ru/')
sleep(5)
browser.save_screenshot(f'./ya_{browser.name.lower()}.png')
browser.quit()'''


#Один скрипт для разных браузеров
'''def make_screen(browser):
    browser.implicitly_wait(15)
    browser.maximize_window()
    browser.get('https://ya.ru/')
    sleep(5)
    browser.save_screenshot(f'./ya_{browser.name.lower()}.png')
    browser.quit()

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
edge = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))

make_screen(chrome)
make_screen(ff)
make_screen(edge)'''

#МЕТОДЫ GET_TITLE AND CURNET_URL
'''browser.get('https://ya.ru/')
browser.title
currnet_title = browser.title
print(currnet_title)
browser.quit()'''


'''browser.get('https://ya.ru/')
url = browser.current_url
print(url)
browser.quit()'''



#РАБОТА С COOKIES
'''my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}
browser.get('https://labirint.ru/')
browser.add_cookie(my_cookie)

browser.refresh()

sleep(8)
browser.quit()'''



#ЧИСТКА COOKIE
'''my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}
browser.get('https://labirint.ru/')
browser.add_cookie(my_cookie)

browser.refresh()
browser.delete_all_cookies()#cookie - можно удалять не все но и по отдельности тоже указывая в форматие ключ значение.

browser.refresh()

sleep(8)
browser.quit()'''




#СБОР ВСЕХ COOKIE
'''my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}
browser.get('https://labirint.ru/')
browser.add_cookie(my_cookie)

coocies = browser.get_cookies()
print(coocies)

browser.refresh()

sleep(8)
browser.quit()'''




#ОБРАЩЕНИЕ К COOKIE
'''my_cookie = {
	'name': 'cookie_policy',
	'value': '1'}

browser.get("https://labirint.ru/")
browser.add_cookie(my_cookie)

cookie = browser.get_cookie('PHPSESSID') #положили метод в переменную cookie
print(cookie) #попросили вывести данных по этой cookie в терминал

browser.refresh()

sleep(10)
browser.quit()'''




#ИЗМЕНЕНИЕ РАЗМЕРОВ ОКНА БРАУЗЕРА
'''browser.get('https://ya.ru/')
browser.implicitly_wait(15)
sleep(2)
browser.maximize_window()
sleep(2)
browser.minimize_window()
sleep(2)
browser.fullscreen_window() #Разворачивает окно браузера на весь экран, скрывая панели инструментов и статус-бар.
sleep(2)
browser.set_window_size(1000, 400)

browser.quit()'''





#РАБОТА С ЭЛЕМЕНТАМИ НА СТРАНИЦЕ
#FIND_ELEMENT
'''browser.get('https://ya.ru/')

element = browser.find_element(By.CSS_SELECTOR, '#text')#поиск элемекнта


print(element)

sleep(5)

browser.quit()'''




#SEND_KEYS
'''browser.get('https://ya.ru/')

element = browser.find_element(By.CSS_SELECTOR, '#text')#поиск элемекнта
element.send_keys('skypro')#отправляем текст

sleep(5)

browser.quit()'''



#CLEAR
'''browser.get('https://ya.ru/')

element = browser.find_element(By.CSS_SELECTOR, '#text')#поиск элемекнта
element.send_keys('skypro')#отправляем текст
sleep(10)#ждем

element.clear()#очищаем
browser.refresh()#обновляем
sleep(10)#ждем

browser.quit() #закрывакм браузер'''





#CLICK
'''browser.get('https://ya.ru/')

element = browser.find_element(By.CSS_SELECTOR, '#text')#поиск элемекнта
element.send_keys('skypro')#отправляем текст
element.send_keys(Keys.RETURN)#нажимаем энтер

sleep(10)#ждем

browser.quit() #закрывакм браузер'''

#ПРИМЕР:
'''browser.get('https://zvyki.com/artist/182306-Vladimir_Kuzmin/')

# Ожидание и поиск элемента
element = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a.no-ajaxy.player-playback.playlist-play[aria-label="слушать Владимир Кузьмин - Моя любовь"]')
    )
)

element.click()
sleep(30)  # или WebDriverWait для следующего действия
browser.quit()'''




#РАБОТА С АТРИБУТАМИ ЭЛЕМЕНТОВ(собираем данные со страницы)
'''browser.get("https://ya.ru")

usd = browser.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]')
txt = usd.text #в переменную с методом text соберется информация об элементе

print(txt) #запрос выведет информацию из переменной в терминал
browser.quit() #закрываем драйвер

browser.quit()'''
#код можно сократить убрав посредника
'''browser.get("https://ya.ru")

usd = browser.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').text

print(usd) #запрос выведет информацию из переменной в терминал
browser.quit() #закрываем драйвер'''



#MЕТОД TAG_NAME
'''browser.get("https://ya.ru")
tag = browser.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').tag_name
print(tag)

browser.quit()'''




#MЕТОД ID
'''browser.get("https://ya.ru")
id_identifier = browser.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').id

print(id_identifier)

browser.quit()'''




#MЕТОД GET_ATRIBUTE
'''browser.get("https://ya.ru")
href = browser.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').get_attribute('href')

print(href)


browser.quit()'''



#MЕТОД VALUE_OF_CSS_PROPERTY( ОТКРЫТЬ COMPUTED )
'''browser.get('https://ya.ru')
ff = browser.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').value_of_css_property('font-family')

print(ff)

browser.quit()'''
####################################################
'''browser.get('https://ya.ru')
fs = browser.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').value_of_css_property('font-size')

print(fs)

browser.quit()'''
####################################################
'''browser.get('https://ya.ru')
color = browser.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').value_of_css_property('color')

print(color)

browser.quit()'''
####################################################
'''browser.get('https://ya.ru')
height = browser.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').value_of_css_property('height')

print(height)

browser.quit()'''
####################################################
'''browser.get('https://ya.ru')
letter_spacing = browser.find_element(By.CSS_SELECTOR, 'a[aria-label^="USD"]').value_of_css_property('letter-spacing')

print(letter_spacing)

browser.quit()'''
####################################################




#MЕТОДЫ IS_ENABLED, IS_DISPLAYED AND IS_SELECTED
#ВИДИМОСТЬ ЭЛЕМЕНТА
#МЕТОД IS_DISPLAED - мы можем отслеживать видимость элементов TRUE - FALSE
# is_displayed() — виден ли элемент для пользователя
# is_enabled() — доступен ли элемент для взаимодействия
# is_selected() — выбран ли элемент (для чекбоксов, радиокнопок)
'''browser.get('http://uitestingplayground.com/visibility')
is_displayed = browser.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()#находим элемент по id и применит к нему метод is_displayed()

print(is_displayed)

sleep(10)

browser.quit()#TRUE'''

#ПРОВЕРКА ВИДИМОСТИ КНОПКИ 0pacity 0;
'''browser.get("http://uitestingplayground.com/visibility") #переход на сайт

#проверка видимости кнопки Opacity 0
is_displayed = browser.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
print(is_displayed) #вывод статуса видимости Opacity 0

browser.find_element(By.CSS_SELECTOR, "#hideButton").click() #нажатие на Hide
# Opacity 0 окажется скрытой
sleep(2)

#еще раз проверим видимость Opacity 0:
is_displayed = browser.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
print(is_displayed) #еще раз выводим статус видимости Opacity 0

sleep(2)

browser.quit()'''
####################################################
#МЕТОД IS_ENABLED - доступен ли элемент для взаимодействия
'''browser.get('https://demoqa.com/radio-button')
is_enabled = browser.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
print(is_enabled)

not_is_enabled = browser.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
print(not_is_enabled)

sleep(5)

browser.quit()#TRUE - False'''
####################################################
#МЕТОД IS_SELECTED - выбран ли элемент (для чекбоксов, радиокнопок - стоит ли галочка в чекбоксе)
'''browser.get("https://the-internet.herokuapp.com/checkboxes")

cb = browser.find_element(By.CSS_SELECTOR, "input[type=checkbox]")

is_selected = cb.is_selected()
print(is_selected)
sleep(3)

cb.click()

is_selected = cb.is_selected()
print(is_selected)
sleep(3)

browser.quit()'''

#РАБОТА С ВЛОЖЕННЫМИ ЭЛЕМЕНТАМИ И ГРУППАМИ ЭЛЕМЕНТОВ
#ПОИСК ЭЛЕМЕНТА ПО HTML
'''browser.get('https://the-internet.herokuapp.com/checkboxes')

div = browser.find_element(By.CSS_SELECTOR, '#page-footer')

tag_a = div.find_element(By.CSS_SELECTOR, 'a')
print(tag_a.get_attribute('href'))

sleep(5)

browser.quit()'''




#МЕТОД FIND_ELEMENTS - поиск множества элементов С БУКВОЙ S НА КОНЦЕ!!!!!! МНОЖЕСТВО ЗНАЧИТ
'''browser.get('https://the-internet.herokuapp.com/checkboxes')
divs = browser.find_elements(By.CSS_SELECTOR, 'div')
l = len(divs)
print(l)

sleep(5)

browser.quit()#8 ЭЛЕМЕНТОВ DIV'''
#РАБОТАЕМ С ИНДЕКСОМ
'''browser.get('https://the-internet.herokuapp.com/checkboxes')
divs = browser.find_elements(By.CSS_SELECTOR, 'div')
div = divs[6]

css_class = div.get_attribute('class')
print(css_class)

sleep(5)

browser.quit()'''


#ОШИБКА ПОИСКА ЭЛЕМЕНТА/ЭЛЕМЕНТОВ - различие еще в том что разная реакция на ошибки


#МЕТОДЫ QUIT AND CLOSE
# driver.close() — если нужно закрыть всплывающее окно, но остаться на основной странице.(закрывает текущую вкладку)
# driver.quit() — в конце тестового сценария, чтобы полностью закрыть браузер и освободить ресурсы.




#ОЖИДАНИЯ : НЕЯВНЫЕ
'''browser.implicitly_wait(10) # seconds

browser.get('https://ya.ru')
textInput = browser.find_element_by_id ('text')

browser.quit()'''

#ОЖИДАНИЯ : ЯВНЫЕ
'''driver.get('https://ya.ru')

#wait 10 seconds before looking for element
element = WebDriverWait (driver, 10).until(
    EC.presence_of_element_located((By.ID, '#text'))
)

browser.quit()'''

#ПРАКТИКА ОЖИДАНИЙ - неявное ожидание
'''browser.implicitly_wait(20)

browser.get("http://www.uitestingplayground.com/ajax")
browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = browser.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

browser.quit()'''

#ПРАКТИКА2 ОЖИДАНИЙ - явное ожидание
waiter = WebDriverWait(driver, 40, 0.1)

driver.get('http://uitestingplayground.com/progressbar')

driver.find_element(By.CSS_SELECTOR, '#startButton').click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#progressBar"), "75%")
)

driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

print( driver.find_element(By.CSS_SELECTOR, "#result").text )

driver.quit()


