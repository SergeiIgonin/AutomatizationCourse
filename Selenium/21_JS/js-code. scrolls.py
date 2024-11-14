"""Использование Javascript"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from scrolls import Scrolls                         # импортируем класс Scrolls из нашего файла scrolls.py для использования его методов
driver = webdriver.Chrome()
action = ActionChains(driver)
scrolls = Scrolls(driver, action)                   # тут еще нужно использовать action, поэтому выше импортируем класс ActionChains


'Скролл страницы. Простой способ'
# Полезно использовать, когда элемент перекрыт другим элементом, напр. футером
driver.execute_script("window.scrollBy(0, 100);")   # альт. метод: driver.execute_script("window.scrollTo(0, +350);")

'Скролл страницы до нужного элемента. Способ с исп. собственного фреймворка'
# Предварительно создадим файл scrolls.py, а в нем создадим класс Scrolls с разными методами скролла.
driver.get("https://seiyria.com/bootstrap-slider/")
time.sleep(2)
my_title = driver.find_element("xpath", "//h3[text()='Example 1: ']")
scrolls.scroll_to_element(my_title)                 # используем один из методов класса Scrolls из нашего файла
time.sleep(2)


'JS-код'
driver.execute_script("alert('Hello World')")       # вызов js-кода на странице, напр. алерта
time.sleep(2)

driver.execute_script("document.title='Script executing';alert('Robots at work');")   # js-код можно писать через запятую
time.sleep(2)

'Остановка (фриз) JS кода для инспектирования элементов dropdown'
# Для этого зафризим код на странице введя в консоль DevTools JS код:
"setTimeout(function() { debugger; }, 5000);"