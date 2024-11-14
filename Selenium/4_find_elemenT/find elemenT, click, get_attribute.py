"""Для поиска ОДНОГО элемента используется метод find_element()"""

from selenium import webdriver
driver = webdriver.Chrome()

'Поиск элементов с модулем BY (не рекомендуется)'
from selenium.webdriver.common.by import By

# 'Пример поиска веб-элемента <input id=”login_field” class="login"/> с модулем By'
# driver.find_element(By.ID, "login_field")       # Поиск по id атрибуту
# driver.find_element(By.CLASS_NAME, "login")     # Поиск по имени класса
# driver.find_element(By.TAG_NAME, "input")       # Поиск по имени тега


'Поиск элементов без модуля BY (вместо него текстовые значения)'
'''
TAG_NAME = "tag name"
ID = "id"
NAME = "name"
CLASS_NAME = "class name"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
CSS_SELECTOR = "css selector"
XPATH = "xpath"
'''
# 'Пример поиска веб-элемента <input id=”login_field” class="login"/> без класса By'
# driver.find_element("id", "123")               # Поиск по id атрибуту
# driver.find_element("class name", "login")     # Поиск по имени класса

'Клик по элементу'
BUTTON_LOCATOR = ("id", "value")                 # запись в переменную локатора элемента
button = driver.find_element(*BUTTON_LOCATOR)    # поиск элемента c распаковкой его локатора
button.click()

'Получить значение атрибута элемента'
print(button.get_attribute("attrib_name"))       # часто применяется в ассертах при смене значений атрибутов

'Получить текст из тела элемента'
print(button.text)                               # часто применяется в ассертах при смене текста


# не для запуска
