"""iframe - это html-страница внутри другой html-страницы"""

import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)

driver.get('https://demoqa.com/nestedframes')
IFRAME_LOCATOR = ("xpath", "//iframe[@id='frame1']")
IFRAME = driver.find_element(*IFRAME_LOCATOR)

'Переключение в iframe и обратно на основную страницу'
# В качестве аргумента можно передавать: локатор веб-элемента, id, атрибут "name", или индекс нужного iframe.
driver.switch_to.frame(IFRAME)                                # переключение в область контента iframe
print(driver.find_element("xpath", "//body").text)  # убедимся, что мы внутри iframe
driver.switch_to.default_content()                            # переключение обратно в основной контент страницы

'Переключение из родительского iframe в дочерний и обратно'
driver.switch_to.frame(IFRAME)
driver.switch_to.frame(0)                                     # проще всего переключаться по индексам дочерних iframe
print(driver.find_element("xpath", "//body").text)  # убедимся, что мы внутри дочернего iframe
driver.switch_to.parent_frame()                               # переключение обратно в родительский iframe
