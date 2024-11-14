"""ДЗ"""
"""
Сайт для выполнения задания: https://demoqa.com/selectable

1. Открыть вкладку Grid
2. Кликнуть на пару любых элементов
3. Убедиться, что они выбраны
4. Кликнуть еще раз и убедиться, что теперь они не выбраны
Советы:
Используйте подход из нюансов) Задача на подумать)
"""

'Выполнение'
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://demoqa.com/selectable")
GREED = ("xpath", "//a[@id='demo-tab-grid']")
driver.find_element(*GREED).click()
ONE = ("xpath", "//li[text()='One']")       # или так ("xpath", "//div[@id='row1']//child::li[1]")
TWO = ("xpath", "//li[text()='Two']")       # или так ("xpath", "//div[@id='row1']//child::li[2]")
driver.find_element(*ONE).click()
driver.find_element(*TWO).click()
assert "active" in driver.find_element(*ONE).get_attribute("class"), "Чекбокс1 не выставлен"
assert "active" in driver.find_element(*TWO).get_attribute("class"), "Чекбокс2 не выставлен"
print('1 pass')
driver.find_element(*ONE).click()
driver.find_element(*TWO).click()
assert "active" not in driver.find_element(*ONE).get_attribute("class"), "Чекбокс1 все еще выставлен"
assert "active" not in driver.find_element(*TWO).get_attribute("class"), "Чекбокс2 все еще выставлен"
print('2 pass')


# АЛЬТЕРНАТИВНОЕ РЕШЕНИЕ С ПОМ. ЦИКЛА FOR
# LOCATORS = [ONE, TWO]
#
# for i in LOCATORS:
#     driver.find_element(*i).click()
#     assert "active" in driver.find_element(*i).get_attribute("class"), "Чекбокс не выставлен"
#     print('passed')
#
# for i in LOCATORS:
#     driver.find_element(*i).click()
#     assert "active" not in driver.find_element(*i).get_attribute("class"), "Чекбокс все еще выставлен"
#     print('passed')
