"""Получение URL открытой страницы и ее заголовка-title (вывод в консоль), валидация полученных данных"""

from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://market.yandex.ru/')

'Получение URL страницы - метод current_url'
page_url = driver.current_url                                       # получение URL страницы записываем в переменную
print('Текущий URL: ', page_url)

'Получение заголовка страницы - метод title'
page_title = driver.title                                           # получение заголовка страницы
print(f'Текущий заголовок: {page_title}')

'Валидация данных - ASSERT'
assert page_url == 'https://market.yandex.ru/', 'Ошибка в URL'      # после запятой пишем свой текс ошибки
assert page_title == 'Интернет-магазин Яндекс Маркет — покупки с быстрой доставкой', 'Страница не открылась'
# assert page_title == 'ГовноМаркет — покупки с долгой доставкой', 'Ошибка в заголовке'  # пример с ошибкой


# 'Получение исходного HTML-кода страницы (в будущем для парсинга и прочих манипуляций)'
# page_source = driver.page_source
# print(page_source)                                                  # распечатать HTML-код всей страницы в терминал
