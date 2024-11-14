"""Скачивание файлов"""

import time
import os
from selenium import webdriver

# 1. Создадим в проекте папку downloads для скачанных файлов.
# 2. Создадим настройку для сохранения скачанных файлов из браузера в эту папку:
preferences = {"download.default_directory": os.path.join(os.getcwd(), "downloads")}   # универсальный путь для всех ОС
# 3. Создадим опцию в которую передадим эти настройки:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", preferences)
# 4. Инициализируем драйвер и добавим в него опции:
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://demoqa.com/upload-download")
download_field = driver.find_element("xpath", "//a[text()='Download']")
download_field.click()
time.sleep(3)
