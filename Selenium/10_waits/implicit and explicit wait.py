"""Ожидания"""

from selenium import webdriver
driver = webdriver.Chrome()

'НЕЯВНЫЕ ОЖИДАНИЯ'
# время, за которое WebDriver будет опрашивать DOM на наличие элементов. Метод подойдет, если элементы долго загружаются.
driver.implicitly_wait(5)   # указывается один раз в коде


'ЯВНЫЕ ОЖИДАНИЯ'
# позволяют настроить ожидания конкретных условий для элементов. Метод подойдет, когда у элементов есть JS настройки.
from selenium.webdriver.support.ui import WebDriverWait             # для указания времени ожидания всех условий
from selenium.webdriver.support import expected_conditions as EC    # дает нам список всех условий
wait = WebDriverWait(driver, 10)                            # создание объекта ожидания

driver.get('URL')
element_locator = ("xpath", "//tag[@attribute='value']")
wait.until(EC.УСЛОВИЕ(element_locator)), 'Кастомный текс ошибки'    # Настроенное ожидание условия (распаковщик "*" уже встроен)
driver.find_element(*element_locator).click()                       # здесь распаковщик нужен

'Основные условия:'
# element_to_be_clickable(locator)              - ожидание видимости и кликабельности элемента.
# visibility_of_element_located(locator)        - ожидание видимости элемента и его присутствия в DOM (шир. и выс. > 0)
# invisibility_of_element_located(locator)      - ожидание невидимости элемента или его исчезновения из DOM.
# text_to_be_present_in_element(locator, text)  - ожидание наличия нужного текста в элементе.
# element_attribute_to_include(locator, value)  - ожидание появления нового атрибута у элемента
