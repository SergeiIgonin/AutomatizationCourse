"""ДЗ"""

'''
На странице https://testautomationpractice.blogspot.com/

1. Найти иконку Wikipedia по имени класса
2. Найти поле ввода Wikipedia по id
3. Найти кнопку поиска Wikipedia по классу
4. Найти любой другой элемент на странице по тегу
'''

'ВЫПОЛНЕНИЕ'
import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://testautomationpractice.blogspot.com/')
print('Иконка: ', driver.find_element('class name', 'wikipedia-icon'))                                  # 1
print('Поле ввода поиск. запроса: ', driver.find_element('id', 'Wikipedia1_wikipedia-search-input'))    # 2
print('Кнопка поиска: ', driver.find_element('class name', 'wikipedia-search-button'))                  # 3
button_new_window = driver.find_elements('tag name', 'button')[0]                                       # 4
print('Кнопка открытия нового окна: ', button_new_window)
button_new_window.click()
time.sleep(1)




