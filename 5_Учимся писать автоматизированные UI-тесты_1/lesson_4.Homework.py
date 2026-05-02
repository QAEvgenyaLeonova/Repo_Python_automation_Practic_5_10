# Импортируем основной модуль Selenium WebDriver, который позволяет управлять браузером
from selenium import webdriver

# Импортируем модуль By — он нужен для указания способа поиска элементов на веб‑странице (по ID, классу, CSS‑селектору и т. д.)
from selenium.webdriver.common.by import By


# Импортируем модуль time — он даёт возможность добавлять паузы в выполнение скрипта (например, чтобы дождаться загрузки страницы)
import time


# Создаём экземпляр драйвера Firefox — запускается браузер Firefox, которым мы будем управлять через код
driver = webdriver.Firefox()

# Открываем в браузере указанную веб‑страницу — в данном случае страницу логина на сайте the‑internet.herokuapp.com
driver.get('https://the-internet.herokuapp.com/login')

# Находим на странице поле для ввода имени пользователя (username) по CSS‑селектору #username (ID элемента)
input_username = driver.find_element(By.CSS_SELECTOR, '#username')
# Вводим в найденное поле текст «tomsmith»
input_username.send_keys('tomsmith')
# Делаем паузу на 1 секунду — даём время на отображение введённых данных и возможную реакцию страницы
time.sleep(1)

# Находим на странице поле для ввода пароля (password) по CSS‑селектору #password (ID элемента)
input_password = driver.find_element(By.CSS_SELECTOR, '#password')
# Вводим в поле пароля текст «SuperSecretPassword!»
input_password.send_keys('SuperSecretPassword!')
# Снова делаем паузу на 1 секунду
time.sleep(1)

# Находим кнопку входа (синяя кнопка с закруглёнными углами) по CSS‑классу .radius
input_blue = driver.find_element(By.CSS_SELECTOR, '.radius')
# Кликаем на найденную кнопку — имитируем нажатие мышью, что запускает процесс авторизации
input_blue.click()

# Ждём 3 секунды — даём время для загрузки следующей страницы после отправки формы
time.sleep(3)

# Закрываем браузер и завершаем сессию WebDriver — корректно освобождаем ресурсы
driver.quit()
