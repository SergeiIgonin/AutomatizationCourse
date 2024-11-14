"""Установка расширений в браузер"""

# Перед автоматической установкой расширения в браузер предварительно нужно:
# 1. скачать нужное расширение в формате.crx на сайте https://www.crx4chrome.com/crx/31939/
# 2. создать в проекте директорию /extensions и положить туда скачанный файл.

'Открытие браузера с использованием расширений'     # например, установим AdBlock (предварительно скачанный)
import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_extension('extensions/adblock.crx')     # указываем путь на файл расширения
driver = webdriver.Chrome(options=options)

driver.get("https://ya.ru/")
list_of_tabs = driver.window_handles
driver.switch_to.window(list_of_tabs[0])            # переключимся на страницу яндекса с рекламной страницы AdBlock
time.sleep(10)                                      # за это время лично убедимся, что расширение успешно установилось
