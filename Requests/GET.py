# В терменале находясь в вирт. окружении установить библиотеку requests:
# > pip(3) install requests

import requests
from requests.auth import HTTPBasicAuth
import pprint                                               # метод для более удобного отображения json формата в консоли
import json

'Структура GET запроса. Распространенные параметры'
# response = requests.get(
#     url="",                                               # endpoint - конечный ресурс (передается в path-параметрах)
#     # auth=HTTPBasicAuth("username", "password"),         # данные аутентификации (сейчас исп. другой метод их передачи - через хэдер)
#     headers={}                                            # словарь, в который передаем аутент. токены и различные хэдеры
#     params={}                                             # query-параметры
#     verify=True                                           # при проблемах с SSL-сертификатом нужно ставить False
# )


'Простой GET-запрос c path-параметрами'                     # path-параметры передаются в конце URL = endpoint (конечный ресурс)
response = requests.get("https://petstore.swagger.io/v2/store/inventory")

'Получение различных данных'
print(response.json())                                      # получить ответ в json формате (если метод не передали сразу в переменную)
print(response.json()['sold'])                              # получить значение по ключу (обращение к элементам словаря)
print(response.status_code)                                 # получить статус-код
print(response.ok)                                          # возвращает True, если статус код меньше 400
print(response.headers)                                     # получить хэдер ответа
print(response.request.headers)                             # получить хэдер запроса
# print(response.text)                                      # получить html разметку страницы
# assert response.json()['sold'] == 5, "Значение не совпадает"  # пример ассерта


'Стандартный GET-запрос'
def test_get_object():      # пример готового теста (Прохождение теста зависит от цифры в pet_id, если ругается на 'id')
    pet_id = 2
    response1 = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}')
    assert response1.ok == True, "Статус-код 400 или выше"
    response1_json = response1.json()
    assert response1_json['id'] == pet_id, "Значение параметра из ответа сервера не совпадает с передаваемым"




'Замена заголовка в хэдере GET-запроса'                     # на примере передачи в хэдер юзер-агента
response = requests.get(
    url="https://petstore.swagger.io/v2/store/inventory",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
)
print(response.request.headers)                             # заново получим хэдер запроса


'GET-запрос c query-параметрами'
response = requests.get(
    url="https://petstore.swagger.io/v2/pet/findByStatus",
    headers={"api_key": "special-key"},
    params={"status": "sold"}
).json()
pprint.pprint(response)


'Скачивание файла GET-запросом'
img_url = "https://www.yaplakal.com/html/static/top-logo.png"
response = requests.get(img_url)
file = open("logo.png", "wb")
file.write(response.content)
# то же самое с помощью контекстного менеджера with:
# with open("logo.png", "wb") as file:
#     file.write(response.content)


# (*) Аутентификация проверяет само право пользователя на доступ в систему (что он есть в базе автор. пользователей)
# (*) Авторизация затем определяет набор прав и уровень доступа пользователя к конкретным ресурсам.
