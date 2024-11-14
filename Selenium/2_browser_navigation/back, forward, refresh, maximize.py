"""Открытие страницы, переход назад и вперед, рефреш"""

import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://market.yandex.ru/')
time.sleep(2)

driver.maximize_window()    # открытие окна браузера во весь экран (но рекомендуется устанавливать размер в опциях (*Lesson8)

# /Вручную перейдем в другой раздел страницы без открытия новой вкладки/

driver.back()               # вернуться назад
time.sleep(2)

driver.forward()            # вернуться вперед
time.sleep(2)

driver.refresh()            # обновить страницу (бывает полезно для очистки введенных данных)
time.sleep(2)
