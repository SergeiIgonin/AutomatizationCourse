"""ДЗ"""

"""
1. Открыть 3 вкладки.
2. Во вкладках перейти на страницы ниже страницы:
    Вкладка 1 - https://hyperskill.org/login
    Вкладка 2 - https://www.avito.ru/
    Вкладка 3 - https://www.ozon.ru/
Так же можете открывать и свои сайты, выше лишь вариант реализации)
3. Вывести в терминал title каждой страницы
4. Кликнуть на любую кнопку или ссылку на каждой странице

Важно:
Сначала нужно открыть все 3 вкладки
Потом получить все title страниц
Потом кликнуть на любой элемент в каждой вкладке
Вариант, когда открыл вкладку получил title и кликнул, потом открыл новую вкладку получил title и кликнул, не подойдет.
Важно походить по вкладкам.
"""

'Выполнение'
import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
options.page_load_strategy = 'eager'
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)

#1
time.sleep(1)
driver.switch_to.new_window("tab")
time.sleep(1)
driver.switch_to.new_window("tab")
time.sleep(1)

#2
list_of_tabs = driver.window_handles
print(len(list_of_tabs))

driver.switch_to.window(list_of_tabs[0])
driver.get("https://hyperskill.org/login")
driver.switch_to.window(list_of_tabs[1])
driver.get("https://www.avito.ru/")
driver.switch_to.window(list_of_tabs[2])
driver.get("https://www.ozon.ru/")

#2
driver.switch_to.window(list_of_tabs[0])
page_title = driver.title
print(f'Текущий заголовок: {page_title}')
driver.switch_to.window(list_of_tabs[1])
page_title = driver.title
print(f'Текущий заголовок: {page_title}')
driver.switch_to.window(list_of_tabs[2])
page_title = driver.title
print(f'Текущий заголовок: {page_title}')

#3
driver.switch_to.window(list_of_tabs[0])
GITHUB_BUTTON = ("xpath", "//main//div/button[2]")
wait.until(EC.element_to_be_clickable(GITHUB_BUTTON))
driver.find_element(*GITHUB_BUTTON).click()
time.sleep(1)
driver.back()
time.sleep(1)

driver.switch_to.window(list_of_tabs[1])
ELECTRONICS_BUTTON = ("xpath", "//img[@alt='Электроника']")
wait.until(EC.element_to_be_clickable(ELECTRONICS_BUTTON))
driver.find_element(*ELECTRONICS_BUTTON).click()
time.sleep(1)
driver.back()
time.sleep(1)

driver.switch_to.window(list_of_tabs[2])
RUB_BUTTON = ("xpath", "//div[text()='RUB']")
wait.until(EC.element_to_be_clickable(RUB_BUTTON))
driver.find_element(*RUB_BUTTON).click()
time.sleep(1)
CLOSE_BUTTON = ("xpath", "(//div[@class='ag013-a'])[4]")
driver.find_element(*CLOSE_BUTTON).click()
time.sleep(1)

driver.quit()
print('all passed')
