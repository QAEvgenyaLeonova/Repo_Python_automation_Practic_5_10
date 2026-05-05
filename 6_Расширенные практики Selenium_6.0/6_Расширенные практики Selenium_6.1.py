# 1_ya.py
from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

try:
    # Попытка установить драйвер Edge
    service = EdgeService(EdgeChromiumDriverManager().install())
    browser = webdriver.Edge(service=service)

    # Настройка окна и переход на страницу
    browser.maximize_window()
    browser.get("https://ya.ru/")  # ОШИБКА В URL!
    sleep(5)

    # Сохранение скриншота и закрытие браузера
    browser.save_screenshot("./ya.png")
    print("Скриншот сохранён успешно!")

except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    if 'browser' in locals():
        browser.quit()
