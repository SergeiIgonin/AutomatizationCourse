"""ДЗ"""
'''
1. Инициализировать драйвер (любой, попробуйте Firefox) p.s: не забудьте его установить.
2. Открыть любую страницу, например: vk.com.
3. Получить и вывести title в консоль.
4. Открыть любую другую страницу, например: ya.ru.
5. Получить и вывести title в консоль.
6. Вернуться назад и, используя assert, убедиться, что вы точно вернулись обратно.
7. Сделать рефреш страницы.
8. Получить и вывести URL-адрес текущей страницы.
9. Вернуться "вперед" на страницу из пункта 4.
10. Убедиться, что URL-адрес изменился.
'''

'ВЫПОЛНЕНИЕ'
import time                                                                  # 1
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://vk.com/')                                                # 2
page1_title = driver.title
print(f'Заголовок страницы ВК: {page1_title}')                               # 3
time.sleep(1)

driver.get('https://ya.ru/')
page2_title = driver.title                                                   # 4
print(f'Заголовок страницы Я.ру: "{page2_title}"')                           # 5
time.sleep(1)

driver.back()                                                                # 6
assert page1_title == 'ВКонтакте | Добро пожаловать', 'Ошибка. Возврат не на ту страницу'
time.sleep(1)

driver.refresh()                                                             # 7

print(driver.current_url)                                                    # 8
time.sleep(1)

driver.forward()                                                             # 9
assert driver.current_url != 'https://vk.com/', 'Ошибка. URL-адрес страницы не изменился'      # 10
time.sleep(1)

driver.close()
