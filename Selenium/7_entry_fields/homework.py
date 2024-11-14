"""ДЗ"""
'''
Задание 1:
1. Заполнить все текстовые поля данными (почистить поля перед заполнением).
2. Проверить, что данные действительно введены, используя get_attribute() и assert.
Страница для выполнения задания: https://demoqa.com/text-box

Задание 2:
1. Прокликать все ссылки со статус-кодами на странице, используя алгоритм перебора элементов (из предыдущих уроков)
2. После каждого клика возвращаться на стартовую страницу.
Страница для выполнения задания: http://the-internet.herokuapp.com/status_codes
'''

'ВЫПОЛНЕНИЕ'
import time
from selenium import webdriver
driver=webdriver.Chrome()

'ЗАДАНИЕ 1'
driver.get('https://demoqa.com/text-box')       # (желательно прописать опцию "eager" (см. Lesson 8)

'Заполнение поля Full Name'
full_name_field = driver.find_element('xpath', '//input[@id="userName"]')
full_name_field.clear()
assert full_name_field.get_attribute('value') == '', 'Поле userName не пустое'
full_name_field.send_keys('Sergei AQA')
assert full_name_field.get_attribute('value') == 'Sergei AQA', 'Данные заполнены не верно или не заполнены'

'Заполнение поля Email'
Email_field = driver.find_element('xpath', '//input[@id="userEmail"]')
Email_field.clear()
assert Email_field.get_attribute('value') == '', 'Поле Email не пустое'
Email_field.send_keys('sigonin@gmail.com')
assert Email_field.get_attribute('value') == 'sigonin@gmail.com', 'Данные заполнены не верно или не заполнены'

'Заполнение поля Current Address'
adress_field = driver.find_element('xpath', '//textarea[@id="currentAddress"]')
adress_field.clear()
assert adress_field.get_attribute('value') == '', 'Поле Current Address не пустое'
adress_field.send_keys('Санкт-Петербург, Испытателей п-т, 20')
assert adress_field.get_attribute('value') == 'Санкт-Петербург, Испытателей п-т, 20', 'Данные заполнены не верно или не заполнены'
print('Задание 1 успешно пройдено')

'ЗАДАНИЕ 2'
driver.get('http://the-internet.herokuapp.com/status_codes')
time.sleep(1)
# Cоздадим список на основе найденных элементов по общему частичному значению их общего атрибута href
sc_list = driver.find_elements('xpath', '//a[contains(@href, "status_code")]')    # метод find_elementS()
for i in sc_list:
    i.click()
    time.sleep(1)
    driver.back()
print('Задание 2 успешно пройдено')

# Аналогичное по сути, но громоздкое, длинное решение:
# sc1 = driver.find_element('xpath', '//a[text()="200"]')
# sc2 = driver.find_element('xpath', '//a[text()="301"]')
# sc3 = driver.find_element('xpath', '//a[text()="404"]')
# sc4 = driver.find_element('xpath', '//a[text()="500"]')
#
# sc_list1 = [sc1, sc2, sc3, sc4]
# for i in sc_list1:
#     i.click()
#     time.sleep(1)
#     driver.back()
