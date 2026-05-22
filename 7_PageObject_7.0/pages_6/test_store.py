import pytest
from selenium import webdriver
from Authorization_Page import AuthorizationPage
from Add_Basket_Page import AddToCart
from Checkout_Basket_Page import Checkout
from Making_Store_Page import MakingStore

@pytest.fixture
def driver(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_store(driver):
    store_auto = AuthorizationPage(driver)
    store_auto.open_driver()
    store_auto.enter_username('standard_user')
    store_auto.enter_password('secret_sauce')
    store_auto.button_click_login()
    store_auto.expectation()

    add_store = AddToCart(driver)
    add_store.add_backpack_basket()
    add_store.add_shirt_basket()
    add_store.add_onesie_basket()
    add_store.button_basket_click()
    add_store.expectation()

    chekout_store = Checkout(driver)
    chekout_store.button_checkout_click()
    chekout_store.expectation()

    making_store = MakingStore(driver)
    making_store.fill_first_name('Евгения')
    making_store.fill_last_name('Леонова')
    making_store.fill_postal_code('123456')
    making_store.click_continue()
    total_amount = making_store.get_count_total()
    assert total_amount == '$58.29', f'Ошибка: сумма не совпадает. Получено: {total_amount}'
    making_store.finish_button()
    making_store.back_to_store()

