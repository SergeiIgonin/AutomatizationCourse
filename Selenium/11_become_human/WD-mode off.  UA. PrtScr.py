"""Имитация человека при управлении браузером: отключение режима WebDriver-mode, подмена юзер-агента. Снятие скриншотов"""

import time
from selenium import webdriver

options = webdriver.ChromeOptions()

'Отключение режима "WebDriver-mode":'
options.add_argument("--disable-blink-features=AutomationControlled")
'Подмена юзер-агента:'
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; rv:125.0) Gecko/20100101 Firefox/125.0")

driver = webdriver.Chrome(options=options)
driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
time.sleep(10)

'Снятие скриншота'
driver.save_screenshot("screen.png")  # в параметр передаем путь сохранения и/или полное имя файла (иначе сохр. в текущей директории)
