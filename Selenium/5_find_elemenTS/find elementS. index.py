"""Метод find_elements() возвращает список одноименных элементов."""
'Полезно, когда необходимо найти группу элементов объединенных чем-то общим'

import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.ozon.ru/')
driver.refresh()
print(driver.title)
elements = driver.find_elements('class name', 'dg6_9')      # (!) elementS (на конце "S")
print(elements)

'Можно вывести текст для всех найденных элементов или только для одного'
for i in elements:
    print(i.text)           # для всех элементов
# print(elements[2].text)   # для одного нужного элемента
# elements[2].click()       # клик по одному нужному элементу
time.sleep(2)

# список одноименных элементов на озоне уже устарел, если что... отдаст пустой массив
