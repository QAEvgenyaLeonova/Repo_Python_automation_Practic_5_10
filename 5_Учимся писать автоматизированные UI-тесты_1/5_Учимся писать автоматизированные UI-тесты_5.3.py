'''
В поле консоли напишите: document.title и нажмите Enter.
Эта команда на языке JavaScript «спрашивает» у страницы, какой у неё 
заголовок (текст в теге <title> HTML-страницы), и выводит его в консоль.

задание_1. Найти локаторы
Локаторы Aviasales

моё решение:
от куда - $$('#avia_form_origin-input')
куда - $$('#avia_form_destination-input')
когда - $$('[data-test-id="start-date-field"]')
обратно - $$('[data-test-id="end-date-field"]')
наити - $$('[data-test-id="form-submit"]')

решение учителя:
Локатор поля Откуда - placeholder="Откуда"
Локатор поля Куда - placeholder="Куда"
Локатор поля Когда - data-test-id="start-date-value
Локатор поля Обратно - data-test-id="end-date-value"
Локатор кнопки Найти билеты - data-test-id="form-submit"

задание_2.Ozon
моё решение:
Локатор кнопки Войти - $x("//div[contains(@class, 'q4b1_4_3-a') and contains(@class, 'cj01_1_11-a')]")
Локатор кнопки Заказы - $$('[href="/my/orderlist/"]')
Локатор выбора валюты (верхний левый угол страницы) - $$('.uw_na9')
Локатор выпадашки Везде (в поисковой строке) - $$('.search_da5')

решение учителя:
Локатор кнопки Войти - //span[text()='Войти']
Локатор кнопки Заказы - //span[text()='Заказы']
Локатор выбора валюты (верхний левый угол страницы) - [data-widget="selectedCurrency"]
Локатор выпадашки Везде (в поисковой строке) - //span[@title='Везде']
'''






'''задание_3'''

'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.example.com')

print(f'Заголовок страницы: {driver.title}')

driver.quit()
'''






'''задание_4'''
'''from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

driver.find_element(By.LINK_TEXT, "Donate").click()

driver.quit()

sleep(10)'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Укажите путь к ChromeDriver (замените на путь к вашему файлу)
service = Service('/path/to/chromedriver')  # например, /usr/local/bin/chromedriver на macOS
driver = webdriver.Chrome(service=service)

# Открываем сайт Python.org
driver.get('https://www.python.org/')

# Находим кнопку "Donate" по классу или тексту (из DOM на скриншоте видно класс "donate-button")
donate_button = driver.find_element(By.CLASS_NAME, "donate-button")

# Кликаем по кнопке
donate_button.click()

# Ждём несколько секунд (опционально)
driver.implicitly_wait(5)

# Закрываем браузер (опционально)
driver.quit()























