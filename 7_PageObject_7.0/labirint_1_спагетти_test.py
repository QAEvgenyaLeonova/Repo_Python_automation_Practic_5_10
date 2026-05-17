import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Кука для согласия с политикой
my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

def test_cart_counter():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        # Открытие сайта лабиринта
        driver.get('https://www.labirint.ru/')
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.add_cookie(my_cookie)

        # Поиск книги по слову "Python"
        search_field = driver.find_element(By.CSS_SELECTOR, '#search-field')
        search_field.send_keys('Python')
        driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

        sleep(1)

        #Добавляем все найденные книги в корзину
        all_button_basket = driver.find_elements(By.CSS_SELECTOR, '.btn-tocart.buy-link')
        counter = 0
        for btn in all_button_basket:
            btn.click()
            counter += 1

        #Проверка и скрытие всплывающей плашки, если она есть
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.popup-window-content.b-basket-popinfo')))
            driver.execute_script("document.querySelector('.popup-window-content.b-basket-popinfo').style.display='none';")
        except:
            pass  # если плашка не появилась, ничего не делаем

        # Вывод общего количества добавленных книг
        print(f"Общее количество добавленных книг: {counter}")

        # Переход в корзину
        sleep(2)
        basket = driver.find_element(By.CSS_SELECTOR, '.b-header-b-personal-e-link.top-link-main.analytics-click-js.cart-icon-js')
        basket.click()

        sleep(2)

        # Получение текста с текущим количеством товаров в корзине
        text_element_book = driver.find_element(By.CSS_SELECTOR, '#basket-default-prod-count2').text
        match = re.search(r'\d+', text_element_book)
        if match:
            number_in_text = int(match.group())
        else:
            raise ValueError('Число не найдено в тексте')

        assert counter == number_in_text, f'Количество в корзине {number_in_text} не совпадает с добавленным {counter}'


    except Exception as e:
        print(f"Произошла ошибка: {e}")
        driver.quit()