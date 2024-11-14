# (*) Сайт для тренировок работы с API: https://petstore.swagger.io/
import pytest
import requests
import pprint


'Стандартный POST-запрос (с отправкой json в теле запроса)'
def test_create_object():       # пример готового теста
    payload={         # (!) body всегда именуем только "json", чтоб не оборачивать кастом. переменные в конструкцию json.dumps({...})
          "id": 5,
          "category": {
            "id": 5,
            "name": "dogs"
          },
          "name": "Rex",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 5,
              "name": "doggie"
            }
          ],
          "status": "available"
        }
    response1 = requests.post(
        url="https://petstore.swagger.io/v2/pet",
        json=payload     # под параметром "json" подразумевается body
    )
    assert response1.ok == True, "Статус-код 400 или выше"
    response1_json = response1.json()
    assert response1_json["name"] == payload["name"], "Значение параметра из ответа сервера не совпадает с передаваемым"
# (!) body всегда именуем только "json", чтоб не оборачивать кастом. переменные в конструкцию json.dumps({...})


'Отправка файла в POST-запросе'
payload = {"file": ("Rex.jpg", open("Rex.jpg", "rb"), "image/jpeg")}
response = requests.post(
    "https://petstore.swagger.io/v2/pet/77/uploadImage",
    headers={
        "api_key": "special-key"
    },
    files=payload     # параметр "files" авт. проставит нужный content-type (в отл. от Postman, где он будет multipart/form_data)
)
print(response.json())
print(response.status_code)
