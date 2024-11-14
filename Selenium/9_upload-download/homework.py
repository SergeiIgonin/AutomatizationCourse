"""ДЗ"""
'''
Задание 1. Загрузить любой файл в 'Choose File'.
Страница для выполнения задания: https://demoqa.com/upload-download

Задание 2. С помощью цикла for скачать все файлы в папку lesson_6/downloads.
Страница для выполнения задания: http://the-internet.herokuapp.com/download
'''

'ВЫПОЛНЕНИЕ'
import os
import time
from selenium import webdriver
preferences = {"download.default_directory": os.path.join(os.getcwd(), "downloads")}
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(options=options)

# 1
driver.get("https://demoqa.com/upload-download")
upload_field = driver.find_element("xpath", "//input[@type='file']")
upload_field.send_keys("D:/Pictures/kusto.jpg")
time.sleep(3)
# 2
driver.get("https://the-internet.herokuapp.com/download")
download_fields = driver.find_elements("xpath", "//a[contains(@href, 'download')]")
print(download_fields)
for i in download_fields:
    i.click()
time.sleep(3)
