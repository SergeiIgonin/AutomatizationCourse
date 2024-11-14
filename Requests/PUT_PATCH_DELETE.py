import requests
import pprint

'PUT-запрос'
# его не рекомендуется использовать, чтоб не потереть чего лишнего:)
def test_update_object():
    payload = {"title": "QWE"}
    response1 = requests.put(url="https://jsonplaceholder.typicode.com/posts/1", json=payload)
    assert response1.ok == True, "Статус-код 400 или выше"
    response1_json = response1.json()
    assert response1_json["title"] == payload["title"], "значение параметра из ответа сервера не совпадает с передаваемым"

# все другие параметры удалились или выставились в 0 (видимо нулевые значения сервер не возвращает)


'PATCH-запрос'
response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={"title": "QWE"}
).json()
pprint.pprint(response)
# изменения затронули только то параметр, которое мы хотели обновить (все остальные параметры на месте)


'DELETE-запрос'                 # (!) Предварительно в этой API нужно создать сущность с таким id POST-запросом (см. файл POST.py)
def test_delete_object():
    pat_id = 5
    response1 = requests.delete(url=f"https://petstore.swagger.io/v2/pet/{pat_id}")
    print(response1.json())
    assert response1.status_code == 200
    response1 = requests.get(f"https://petstore.swagger.io/v2/pet/{pat_id}")
    assert response1.status_code == 404
