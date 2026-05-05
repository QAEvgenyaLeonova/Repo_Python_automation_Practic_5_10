from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/checkboxes")

divs = driver.find_elements(By.CSS_SELECTOR, 'div')

div = divs[6]
css_class = div.get_attribute('class')

print(css_class)

driver.quit()