"""Устаревший Dropdown — выпадающий список пунктов с тегом <select>"""

from selenium import webdriver
from selenium.webdriver.support.select import Select           # импортируем класс Select для работы с dropdown старого образца
driver = webdriver.Chrome()

driver.get("https://demoqa.com/select-menu")
DROPDOWN_LOCATOR = ("xpath", "//select[@id='oldSelectMenu']")  # определяем локатор элемента dropdown
dropdown = Select(driver.find_element(*DROPDOWN_LOCATOR))      # определяем его как объект для взаимодействия типа select (так надо)
dropdown.select_by_value("2")                                  # выбираем нужный нам пункт по значению value (рекоменд. способ)
# DROPDOWN.select_by_index(4)                                  # выбор пункта по index
# DROPDOWN.select_by_visible_text("Indigo")                    # выбор пункта по содержимому text


'Перебор (выбор) всех пунктов выпадающего списка'              # для проверки их доступности к выбору
all_options = dropdown.options                                 # спец. атрибут options возвращает список всех пунктов
for i in all_options:
    dropdown.select_by_value(i.get_attribute("value"))
print('passed')

# Альтернативные способы перебора:
# перебор пунктов по индексу: DROPDOWN.select_by_index(all_options.index(option))
# перебор пунктов по тексту: DROPDOWN.select_by_visible_text(option.text)
