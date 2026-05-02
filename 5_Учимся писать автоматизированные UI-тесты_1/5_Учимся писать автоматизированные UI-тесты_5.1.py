from selenium import webdriver

driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/") #браузер откроет страницу
driver.get("https://vk.com/") #перейдет на следующую страницу
driver.set_window_size(640, 460) #окно браузера уменьшится под параметры
#driver.maximize_window #открыть окно по размеру экрана
#driver.minimize_window #свернуть окно браузера
#driver.fullscreen_window #развернуть окно на весь экран, аналог F11
#driver.back() #назад
#driver.forward() #Вперед
#driver.refresh() #Обновить


sleep(3)

driver.save_screenshot('./ya.png')

#https://www.selenium.dev/documentation/ - get
#https://www.selenium.dev/documentation/webdriver/interactions/navigation/ - back
#https://www.selenium.dev/documentation/webdriver/elements/finders/ - driver.find_element(By.CLASS_NAME, "tomatoes") #видим неопознанный класc By
#https://www.selenium.dev/documentation/webdriver/actions_api/keyboard/ - send_keys/ from selenium.webdriver.common.keys import Keys
#https://www.selenium.dev/documentation/webdriver/elements/information/#text-content - подсказывает, как вывести информацию из элемента

'''Selenium с Python для тестировщика: «версия для первоклассника»
1. Что такое Selenium + Python?
Это «волшебный пульт», который позволяет компьютеру самому щёлкать по кнопкам, заполнять формы, переходить по ссылкам на сайтах — как будто человек сидит за компьютером. Python — простой язык, который помогает Selenium понимать команды.

2. Как начать?

Устанавливаем Selenium: в терминале пишем $ pip install selenium.
Импортируем библиотеку: from selenium import webdriver.
Запускаем «водитель» (driver) для браузера — он будет управлять сайтом:
для Chrome: driver = webdriver.Chrome();
для Firefox: driver = webdriver.Firefox();
для Safari: driver = webdriver.Safari() и т. д.
3. Базовые команды (как заклинания)

Открыть сайт: driver.get("https://сайт.ру").
Обновить страницу: driver.refresh().
Ввести текст в поле: элемент.send_keys("текст").
Нажать на элемент (кнопку, ссылку): элемент.click().
Очистить поле: элемент.clear().
4. Как найти «кнопку» или «поле» на сайте? (поиск сокровищ)

Есть несколько «магических слов» для поиска:

По ID: driver.find_element_by_id("id_элемента").
По классу: driver.find_element_by_class_name("имя_класса").
По имени: driver.find_element_by_name("имя").
По XPath (точный путь к элементу): driver.find_element_by_xpath("//input[@name='email']").
По тегу (например, INPUT, DIV): driver.find_element_by_tag_name("input").
По тексту ссылки: driver.find_element_by_link_text("Текст ссылки").
По части текста ссылки: driver.find_element_by_partial_link_text("Часть текста").
5. Специальные трюки

Перетаскивать элементы: ActionChains(driver).drag_and_drop(элемент, цель).perform().
Выбирать пункты в выпадающем списке: Select(элемент).select_by_index(номер) или select_by_visible_text("текст").
Переключаться между окнами: driver.switch_to_window("имя_окна").
Работать с iFrame (встроенными страницами): driver.switch_to_frame("имя_iframe").
Обрабатывать всплывающие окна:
принять: alert_obj.accept();
отклонить: alert_obj.dismiss();
прочитать текст: alert_obj.text().
6. Навигация по истории браузера

назад: driver.back();
вперёд: driver.forward().
7. Работа с cookie (маленькими «записками» сайта)

добавить: driver.add_cookie({'name': 'user', 'value': 'vinayak'});
получить все: driver.get_cookies();
удалить: driver.delete_cookie(cookie) или driver.delete_all_cookies().
8. Ожидания (чтобы Selenium не торопился)

Неявное ожидание (ждёт фиксированное время перед поиском элемента): driver.implicitly_wait(10) (в секундах).
Явное ожидание (ждёт, пока выполнится условие): WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_элемента"))).
9. Скриншоты (чтобы запомнить, что случилось) driver.save_screenshot('путь_к_файлу.png') — делает снимок экрана.

10. Настройка окна браузера driver.set_window_size(1200, 800) — задаёт размер окна (ширина, высота).

Итог: Selenium + Python — это «робот-тестировщик», который умеет:

ходить по сайтам;
заполнять формы;
щёлкать кнопки;
делать скриншоты;
ждать, когда сайт загрузится;
работать с окнами, списками, всплывающими сообщениями.'''























