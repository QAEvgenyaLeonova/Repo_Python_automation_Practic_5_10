import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
from calculator_locators import CalcLocatorsPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator_delay(driver):
    form_calc = CalculatorPage(driver)
    form_calc.open_driver()
    form_calc.set_delay('45')
    form_calc.click_buttun(CalcLocatorsPage.BUTTON_SEVEN)
    form_calc.click_buttun(CalcLocatorsPage.BUTTON_PLUS)
    form_calc.click_buttun(CalcLocatorsPage.BUTTON_EIGHT)
    form_calc.click_buttun(CalcLocatorsPage.BUTTON_EQUALLY)

    result = form_calc.get_result()
    assert result =='15' , f'Ожидается результат 15, но получен {result}'

