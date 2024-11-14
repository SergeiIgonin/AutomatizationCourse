"""Современный Dropdown — меню выбора с тегом <div>//<input>"""
# Визуально реализован как dropdown (селект) или текстовое поле (мультиселект) с выбором одного/нескольких пунктов

from selenium import webdriver
from selenium.webdriver import Keys
driver = webdriver.Chrome()

driver.get("https://demoqa.com/select-menu")
# в первую очередь нужно отыскать тег <input> в структуре искомого элемента (обычно <div>//<input>):
SELECT_LOCATOR = ("xpath", "//input[@id='react-select-3-input']")
driver.find_element(*SELECT_LOCATOR).send_keys("Mrs.")              # Вводим в dropdown название пункта (для его выбора)
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)          # Подтверждаем выбор нажатием ENTER

'Остановка (фриз) JS кода для инспектирования элементов dropdown'
# Казалось бы, можно сделать проще — просто кликнуть на dropdown, а потом по нужному пункту.
# Но тут возникнет проблема — при попытке инспектирования пункта, dropdown будет сворачиваться (т.к. мы отводим от него курсор).
# Для этого зафризим код на странице введя в консоль DevTools JS код:
"setTimeout(function() { debugger; }, 5000);"
# Т.е. запустим JS код, раскроем dropdown и, дождавшись фриза, спокойно проинспектируем нужный нам элемент для клика.

'Доступен выбор пункта по частичному вводу его названия'
# Вводимый нами текст подставляется в значение атрибута value, но после подтверждения выбора он становится пустым.
# Т.е. уже выбранное значение не хранится в атрибуте value.
# Можно проверить, что вводимый нами текст подставляется в значение атрибута value:
driver.get("https://demoqa.com/select-menu")
multiselect = driver.find_element("xpath", "//input[@id='react-select-4-input']")
multiselect.send_keys("Gre")
assert multiselect.get_attribute("value") == "Gre", "Текст не введен"
multiselect.send_keys(Keys.ENTER)
