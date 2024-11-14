"""ДЗ"""
"""
Задание 1 (Установка и чтение куки)
  - Откройте любой сайт и добавьте куки с именем "username" и значением "user123".
  - Затем обновите страницу и убедитесь, что кука "username" была успешно установлена.
  - Получите и провалидируйте значение куки "username" и выведите его на экран.

Задание 2 (Удаление куков)
  - Откройте любой сайт и через Devtools выберете куку.
  - Удалите выбранную куку.
  - После удаления куки, обновите страницу и проверьте, что она отсутствует.

Задание 3 (Автоматизация корзины покупок)
  - Напишите сценарий, который использует Selenium WebDriver для автоматического добавления товаров в корзину, в интернет-магазине.
  - После добавления товаров, сохраните состояние корзины, записав куки в переменную или файл.
  - Затем удалите все товары из корзины, очистив все куки и перезагрузив страницу.
  - Восстановите сессию путем подставления ранее сохраненных куков и перезагрузкой странцы после.

Заметки:
Используйте режим отключения WebDriver и User-agent
"""

import time
import pickle
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; rv:125.0) Gecko/20100101 Firefox/125.0")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 3)


# 1
url = 'https://www.ozon.ru/'
driver.get(url)
driver.add_cookie({
    'name': 'username',
    'value': 'user123'
})
driver.refresh()
my_cookie = driver.get_cookie('username')
print(my_cookie)
assert my_cookie['value'] == 'user123', 'Ошибка в значении куки'
cookies = driver.get_cookies()
assert my_cookie in cookies, "Кука не добавилась"
print('1 passed')

# 2
driver.get(url)
my_cookie = driver.get_cookie("__Secure-user-id")
driver.delete_cookie("__Secure-user-id")
driver.refresh()
cookies = driver.get_cookies()
assert my_cookie not in cookies, "Кука не удалилась"
print('2 passed')

# 3
url2 = ('https://www.ozon.ru/product/honor-smartfon-x8b-rostest-eac-8-256-gb-chernyy-1577351278/?asb=xeW4BMtfjxMedqME7Z5TRfIC6e4HT0'
        'mRChri%252FGRoTZA%253D&asb2=YEMf7wwU1c3Z3zu9OLAVxdkhHc7vGIIYbuGKLQVj-sbQU6e0BdB6v0ttiIJRc1X_heHVARbWJaeOCOSEo5rYYQ&avtc=1&'
        'avte=2&avts=1723657744&keywords=honor+x8b+%D1%81%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD')
driver.get(url2)

ADD_BUTTON = ("xpath", "(//button[@class='q5k_27 b2111-a0 b2111-b2 b2111-a4'])[1]")
wait.until(EC.element_to_be_clickable(ADD_BUTTON), 'Кнопка добавления товара в корзину не кликабельна')
driver.find_element(*ADD_BUTTON).click()

KART_INDICATOR = ("xpath", "//span[text()='1'][1]")
wait.until(EC.visibility_of_element_located(KART_INDICATOR), 'Значение индикатора на иконке корзины не обновилось')

KART_ICON = ("xpath", "//a[@data-widget='headerIcon']")
wait.until(EC.element_to_be_clickable(KART_ICON), 'Иконка корзины не кликабельна')
driver.find_element(*KART_ICON ).click()

ITEM = ("xpath", "//div[@class='b2o_4_6 ob2_4_6']")
wait.until(EC.visibility_of_element_located(ITEM), 'Товар отсутствует в корзине')

pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))
driver.delete_all_cookies()
driver.refresh()
time.sleep(3)
cookies_list = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
for i in cookies_list:
    driver.add_cookie(i)
driver.refresh()
time.sleep(3)
print('3 passed')
