import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = None

def open_labirint():
    global driver, wait
    driver.get('https://www.labirint.ru/')
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.add_cookie(my_cookie)
    wait = WebDriverWait(driver, 10)

def search(term):
    search_field = driver.find_element(By.CSS_SELECTOR, '#search-field')
    search_field.clear()
    search_field.send_keys(term)
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

def add_books():
    all_button_basket = driver.find_elements(By.CSS_SELECTOR, '.btn-tocart.buy-link')
    counter = 0
    for btn in all_button_basket:
        btn.click()
        counter += 1
        sleep(1)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.popup-window-content.b-basket-popinfo')))
        driver.execute_script("document.querySelector('.popup-window-content.b-basket-popinfo').style.display='none';")
    except:
        pass
    return counter

def get_to_card():
    basket = driver.find_element(By.CSS_SELECTOR, '.b-header-b-personal-e-link.top-link-main.analytics-click-js.cart-icon-js')
    basket.click()
    sleep(2)
    text_element_book = driver.find_element(By.CSS_SELECTOR, '#basket-default-prod-count2').text
    match = re.search(r'\d+', text_element_book)
    if match:
        number_in_text = int(match.group())
    else:
        raise ValueError('Число не найдено в тексте')
    return number_in_text

def close_driver():
    driver.quit()

def get_title():
    return driver.find_element(By.CSS_SELECTOR, '.search-title').text

def test_cart_counter():
    global wait
    open_labirint()
    search('python')
    added = add_books()
    cart_counter = get_to_card()
    close_driver()
    print(f"Добавлено книг: {added}")
    print(f"В корзине отображается: {cart_counter}")
    assert added == cart_counter, f"Количество в корзине {cart_counter} не совпадает с добавленным {added}"

def test_search_title():
    global wait
    open_labirint()
    search('no book search term')
    txt = get_title()
    expected_title = 'Все, что мы нашли в Лабиринте по запросу «no book search term»'
    close_driver()
    assert txt == expected_title, f"Ожидаемый заголовок: '{expected_title}', но получен: '{txt}'"
