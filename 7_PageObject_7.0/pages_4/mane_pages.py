from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service as EdgeService

def test_form_validation_colors():
    edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))
    wait = WebDriverWait(driver, 15)

    try:
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        driver.maximize_window()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="first-name"]'))).send_keys('Иван')
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="last-name"]'))).send_keys('Петров')
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="address"]'))).send_keys('Ленина, 55-3')
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="e-mail"]'))).send_keys('test@skypro.com')
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="phone"]'))).send_keys('+7985899998787')

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="zip-code"]'))).send_keys('')

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="city"]'))).send_keys('Москва')
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="country"]'))).send_keys('Россия')
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="job-position"]'))).send_keys('QA')
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="company"]'))).send_keys('SkyPro')


        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-outline-primary')))
        driver.execute_script('arguments[0].scrollIntoView({block: "center"});', submit_button)
        actions = ActionChains(driver)
        actions.move_to_element(submit_button).click().perform()


        WebDriverWait(driver, 5).until(lambda d: d.execute_script('return document.readyState') == 'complete')


        wait.until(EC.visibility_of_element_located((By.ID, 'first-name')))
        wait.until(EC.visibility_of_element_located((By.ID, 'last-name')))
        wait.until(EC.visibility_of_element_located((By.ID, 'address')))
        wait.until(EC.visibility_of_element_located((By.ID, 'e-mail')))
        wait.until(EC.visibility_of_element_located((By.ID, 'phone')))
        wait.until(EC.visibility_of_element_located((By.ID, 'zip-code')))
        wait.until(EC.visibility_of_element_located((By.ID, 'city')))
        wait.until(EC.visibility_of_element_located((By.ID, 'country')))
        wait.until(EC.visibility_of_element_located((By.ID, 'job-position')))
        wait.until(EC.visibility_of_element_located((By.ID, 'company')))

        zip_code_element = driver.find_element(By.ID, 'zip-code')
        background_color_zip = zip_code_element.value_of_css_property('background-color')
        print('Цвет поля ZIP-code:', background_color_zip)


        expected_red = 'rgba(248, 215, 218, 1)'
        assert background_color_zip == expected_red, "Поле ZIP-code не подсвечено красным"


        fields_ids = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country', 'job-position', 'company']
        expected_green = 'rgba(209, 231, 221, 1)'

        for field_id in fields_ids:
            element = driver.find_element(By.ID, field_id)
            color = element.value_of_css_property('background-color')
            print(f'Цвет поля {field_id}:', color)
            assert color == expected_green, f"Поле {field_id} не подсвечено зеленым"

    finally:
        driver.quit()

