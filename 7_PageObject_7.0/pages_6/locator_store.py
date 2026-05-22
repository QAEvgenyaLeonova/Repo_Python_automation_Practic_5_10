from selenium.webdriver.common.by import By

class Store:
    INPUT_NAME = (By.CSS_SELECTOR, '#user-name')
    INPUT_PASS = (By.CSS_SELECTOR, '#password')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '#login-button')
    ADD_BACKPACK_BASKET = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_SHIRT_BASKET = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ADD_ONESIE_BASKET = (By.ID, 'add-to-cart-sauce-labs-onesie')
    BASKET = (By.CSS_SELECTOR, '.shopping_cart_link')
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, '#checkout')
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    INDEX_COD = (By.ID, 'postal-code')
    BUTTON_CONTINUE = (By.ID, 'continue')
    TOTAL_ELEMENT = (By.CSS_SELECTOR, 'div.summary_total_label')
    BUTTON_FINISH = (By.CSS_SELECTOR, '#finish')
    BUTTON_BACK = (By.CSS_SELECTOR, '#back-to-products')

