from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
waiter = WebDriverWait(driver, 40, 0.1)

driver.get('http://uitestingplayground.com/progressbar')

driver.find_element(By.CSS_SELECTOR, '#startButton').click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#progressBar"), "75%")
)

driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

print( driver.find_element(By.CSS_SELECTOR, "#result").text )

driver.quit()
