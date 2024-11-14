"""Работа с алертами. Алерты не являются элем. DOM"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/alerts")

BUTTON_1 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()    # ожидание и клик по кнопке, которая вызывает alert (распаковщик встроен)
wait.until(EC.alert_is_present())                           # ожидание появления alert
alert = driver.switch_to.alert                              # запись alert в переменную и переключение на него
time.sleep(2)
print(alert.text)                                           # вывод текста из алерта
alert.send_keys("Hello world")                              # ввод текста в поле алерта
time.sleep(2)
alert.accept()                                              # принять алерт
time.sleep(5)
# alert.dismiss()                                            # отклонить алерт
