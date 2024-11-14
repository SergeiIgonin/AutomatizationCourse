"""Работа с чекбоксами и радиокнопками"""
# Чекбоксы могут иметь разный внешний вид, но чаще реализуются с помощью тега <input>, но с type=’checkbox’

from selenium import webdriver
driver = webdriver.Chrome()

'Выставление чекбокса методом click()'
CHECKBOX = ("xpath", "//selector")
driver.find_element(*CHECKBOX).click()

'Проверка статуса чекбокса (выставлен/не выставлен)'
CHECKBOX_1 = ("xpath", "//selector1")       # выставленный
CHECKBOX_2 = ("xpath", "//selector2")       # не выставленный
# Способ 1. С помощью метода is_selected() — метод возвращает True или False
assert driver.find_element(*CHECKBOX_1).is_selected() is True, "Чекбокс не выбран"
assert driver.find_element(*CHECKBOX_2).is_selected() is False, "Чекбокс до сих пор выбран"
# Способ 2. С помощью метода get_attribute('name') — метод принимает в аргументе имя атрибута, а возвращает его значение
assert driver.find_element(*CHECKBOX_1).get_attribute("checked") is not None    # что чекбокс выставлен
assert driver.find_element(*CHECKBOX_2).get_attribute("checked") is None        # что чекбокс не выставлен

'Нюанс 1'
# Ситуации, когда при попытке выставить чекбокс выходит ошибка 'ElementNotInteractableException: Message: element not interactable'
# Все потому, что чекбокса перекрыт другими элементами и недоступен для взаимодействия (пример тут: https://demoqa.com/checkbox)
# Но т.к. часто можно кликнуть на любой элемент, лежащий в одной компоненте с чекбоксом, то тогда ->
# нужно работать по принципу: 1 элемент для клика и 1 элемент для проверки статуса.

'Нюанс 2'
# Ситуация, когда в целом реализация чекбоксов не предполагает тег <input> (пример тут: https://demoqa.com/selectable)
# Покликав на элементе можно заметить, что в его класс добавляется/исчезает новый класс "active".
# Сделаем проверку опираясь на этот факт:
assert "active" in driver.find_element(*FIRST_CHECKBOX).get_attribute("class"), "Чекбокс не выбран"


'РАДИОКНОПКИ'       # суть и методы те же, что у чекбоксов
'Проверка доступности/недоступности радиокнопки для выставления'    # пример тут: https://demoqa.com/radio-button
assert driver.find_element(*NO_RADIO_BUTTON).is_enabled() is False


