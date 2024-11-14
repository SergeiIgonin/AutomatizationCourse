"""Работа с вкладаками/окнами"""
# WebDriver не видит разницы между окнами и вкладками.
# Статус авторизации распространяется на всю сессию работы с сайтом, независимо от кол-ва открытых в нем вкладок.
# Каждая вкладка или окно имеют дескриптор - уникальный идентификатор сохраняющийся в течении одного сеанса.

import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)

driver.get("https://hyperskill.org/login")
time.sleep(2)

'Получение дескриптора (ID) текущей активной вкладки/окна'
main_tab = driver.current_window_handle
print("Дескриптор начальной вкладки: ", main_tab)          # запись дескриптора вкладки в переменную

# Кликнем по кнопке, которая открывает новую вкладку:
FOR_BUSINESS_BUTTON = ("xpath", "//a[text()=' For Business ']")
driver.find_element(*FOR_BUSINESS_BUTTON).click()
time.sleep(2)

'Получение списка дескрипторов всех открытых вкладок/окон'
list_of_tabs = driver.window_handles
print("Список дескрипторов всех открытых вкладок/окон: ", list_of_tabs)
print("Длина списка дескрипторов всех открытых вкладок/окон: ", len(list_of_tabs))

'Переключение фокуса на другую вкладку по ее индексу'
driver.switch_to.window(list_of_tabs[0])                    # нумерация по списку нач. с 0
time.sleep(2)
new_tab = driver.current_window_handle                      # запишем дескриптор новой (активной) вкладки в переменную
print("Дескриптор новой вкладки: ", new_tab)

'Получение индекса вкладки/окна (для информативности)'
print("Индекс начальной вкладки: ", list_of_tabs.index(main_tab))
print("Индекс новой вкладки: ", list_of_tabs.index(new_tab))

'Проверка факта переключения на новую вкладку (дескриптор другой)'
assert new_tab != main_tab, "Ошибка переключения между вкладками"

# Кликнем по кнопке, расположенной на новой вкладке:
START_FOR_FREE_BUTTON = ("xpath", "(//a[text()='Start for Free'])[1]")
driver.find_element(*START_FOR_FREE_BUTTON).click()
time.sleep(2)

'Открытие новых вкладок и окон с переключением на них'
driver.switch_to.new_window("tab")
time.sleep(2)
driver.switch_to.new_window("window")
time.sleep(2)

'Закрытие вкладки/окна'
driver.close()              # Закрытие активного окна/вкладки
time.sleep(2)

'Закрытие браузера'
driver.quit()               # Закрытие сессии, т.е всего браузера
