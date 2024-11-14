"""Ввод с клавиатуры"""

from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver import Keys                                # импортируем класс Keys для работы с клавиатурой

driver.get('https://demoqa.com/automation-practice-form')
INPUT_FIELD = ("xpath", "//input[@id='firstName']")
driver.find_element(*INPUT_FIELD).send_keys("Hello World")         # Ввод текста в поле
driver.find_element(*INPUT_FIELD).send_keys(Keys.CONTROL + "A")    # Выделение текста
driver.find_element(*INPUT_FIELD).send_keys(Keys.BACKSPACE)        # Удаление выделенного


'Копипастим используя работу с клавиатурой'
driver.get("https://demoqa.com/date-picker")
copy_field = driver.find_element("xpath", "//input[@id='dateAndTimePickerInput']")
past_field = driver.find_element("xpath", "//input[@id='datePickerMonthYearInput']")
past_field.send_keys(Keys.CONTROL + "A")                            # Выделяем текст в поле для вставки копипасты
past_field.send_keys(Keys.BACKSPACE)                                # Удаляем выделенное
copy_field.send_keys(Keys.CONTROL + "A")                            # Выделяем текст в поле откуда будем копировать
copy_field.send_keys(Keys.CONTROL + 'C')                            # Копируем выделенное
past_field.send_keys(Keys.CONTROL +'V')                             # Вставляем скопированный текст в поле для вставки
