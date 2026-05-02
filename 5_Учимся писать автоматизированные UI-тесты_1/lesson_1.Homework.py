from selenium import webdriver  # Импортируем модуль webdriver из библиотеки Selenium — нужен для управления браузером
from selenium.webdriver.chrome.service import Service as ChromeService  # Импортируем класс Service (переименовываем в ChromeService) для настройки сервиса ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager  # Импортируем ChromeDriverManager — утилита для автоматической загрузки и управления драйвером Chrome
from selenium.webdriver.common.by import By  # Импортируем enum By для указания способа поиска элементов (по ID, классу, тексту и т. д.)
from selenium.webdriver.support.ui import WebDriverWait  # Импортируем WebDriverWait для явного ожидания выполнения условий (например, пока элемент станет кликабельным)
from selenium.webdriver.support import expected_conditions as EC  # Импортируем модуль expected_conditions (сокращённо EC) — набор предустановленных условий для WebDriverWait
import time  # Импортируем модуль time для работы с задержками (пауза в выполнении скрипта)

# Настройка драйвера Chrome
service = ChromeService(executable_path=ChromeDriverManager().install())  # Создаём объект ChromeService, указываем путь к драйверу. ChromeDriverManager().install() автоматически скачивает и устанавливает подходящий драйвер Chrome
driver = webdriver.Chrome(service=service)  # Создаём экземпляр драйвера (открываем браузер Chrome), передаём настройки сервиса

try:  # Начинаем блок try — здесь размещаем основной код, который может вызвать исключения
    # Открытие страницы
    driver.get('http://uitestingplayground.com/classattr')  # Открываем указанную веб-страницу в браузере
    driver.implicitly_wait(10)  # Устанавливаем неявное ожидание (до 10 секунд) для всех последующих поисков элементов. Если элемент не найден сразу — Selenium будет ждать до 10 секунд перед ошибкой

    # Поиск синей кнопки по CSS-классу btn-primary
    blue_button = WebDriverWait(driver, 10).until(  # Создаём объект ожидания (до 10 секунд) и ждём, пока условие станет истинным
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))  # Условие: элемент с CSS-классом "btn-primary" должен стать кликабельным. By.CSS_SELECTOR указывает способ поиска по CSS-селектору
    )  # Найденный элемент сохраняем в переменную blue_button

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))  # Дополнительное ожидание (5 секунд) — ждём, пока элемент станет видимым. Эта строка избыточна, так как element_to_be_clickable уже подразумевает видимость элемента

    # Клик по кнопке
    blue_button.click()  # Выполняем клик по найденному элементу (синей кнопке)
    print("Клик по синей кнопке выполнен!")  # Выводим сообщение в консоль, подтверждающее выполнение клика

    time.sleep(5)  # Пауза на 5 секунд — даёт время увидеть результат клика (например, появление алерта или изменение страницы). В продакшн-коде лучше заменить на явное ожидание нужного состояния страницы

finally:  # Блок finally выполняется всегда, независимо от успеха/неудачи в блоке try
    # Закрытие браузера после выполнения
    driver.quit()  # Закрываем браузер и освобождаем ресурсы (важно для предотвращения утечек памяти)
