import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage

'''def test_cart_counter():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    main_page = MainPage(driver)
    main_page.set_ccokie_policy()
    main_page.search('python')

    result_page = ResultPage(driver)
    to_be = result_page.add_books()

    cart_page = CartPage(driver)
    cart_page.get()
    as_is = cart_page.get_counter()

    assert as_is == to_be
    sleep(5)
    driver.quit()'''

def test_empty_search_result():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    main_page = MainPage(driver)
    main_page.set_ccokie_policy()
    main_page.search('no book search term')

    result_page = ResultPage(driver)
    mssg = result_page.get_empty_result_message()

    assert mssg == 'Все, что мы нашли в Лабиринте по запросу «no book search term»'
    print("Текст сообщения:", mssg)

    driver.quit()