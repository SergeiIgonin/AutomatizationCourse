"""Работа с использованием прокси-сервера"""

import time
from selenium import webdriver

PROXY = "79.137.136.254:8079"                       # Записываем в переменную IP адрес и порт прокси-сервера
# PROXY = "username:password@37.19.220.129:8443"    # Авторизация в прокси-сервере (если требуется) — просто подставляем свои данные
# вариант с авторизацией будет работать только при наличии расширений типа undetected_chromedriver или selenium-wire.
options = webdriver.ChromeOptions()
options.add_argument(f"--proxy-server={PROXY}")     # Добавляем прокси через опции
# Синтаксис: (f'--proxy-server=ip_proxy:port_proxy')
driver = webdriver.Chrome(options=options)
driver.get("https://2ip.ru")                        # Проверяем текущий IP-адрес на спец. сайте
time.sleep(5)

# В итоге:
# мой IP без использования прокси: 88.201.168.53
# мой IP с прокси:

# P.S. говорят, что для работы с проксей предварительно нужно установить соответствующее расширение, но какое?..
