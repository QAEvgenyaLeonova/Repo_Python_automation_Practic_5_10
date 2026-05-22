from time import sleep
import pytest
from selenium import webdriver
from main_page import GoogleMainePage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com/')
    yield driver
    sleep(5)
    driver.quit()

def test_search(driver):
    page = GoogleMainePage(driver)
    page.search_for('Selenium')
    results = page.get_search_results()

    assert len(results) > 0, 'Результаты поиска не найдены'


