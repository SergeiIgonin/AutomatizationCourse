"""Инициализация веб-драйверов"""

'Инициализация драйвера Chrome:'
from selenium import webdriver
driver = webdriver.Chrome()

'Инициализация драйвера Firefox:'
from selenium import webdriver
driver = webdriver.Firefox()
driver.close()


'Объявление нужного языка браузера для Firefox'
fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)
# Для хрома это делается через опции (см. 8_options)


'Инициализация через WebDriverManager (у меня так не работает)'
# !!! Chrome:
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# !!! Firefox:
# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service
#
# service = Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=service)
