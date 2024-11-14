"""Загрузка файлов"""

import os
import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://demoqa.com/upload-download")
upload_field = driver.find_element("xpath", "//input[@type='file']")
upload_field.send_keys("D:/ВАЖНО/main_кусто.jpg")                       # в аргументе указываем путь к файлу на ПК
# upload_field.send_keys(f'{os.getcwd()}/downloads/sampleFile.jpeg')    # способ для загрузки файлов из папки downloads
time.sleep(3)

# (!) если загрузка файлов на странице реализована через кнопку, то нужно искать скрытый элемент //input[@type=”file”]
# (!) Для Windows, все пути к файлам и т.д, необходимо прописывать с обратным слешем! Иногда даже с двойным.
