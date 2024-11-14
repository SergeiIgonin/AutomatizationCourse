"""Динамические фикстуры. Параметризация тестов для запуска с разными тестовыми данными"""
# В фикстуру сначала передаем кастом. параметр (который затем вместо себя будет подставлять значения из списка), затем список c данными

import pytest
from selenium import webdriver
driver = webdriver.Chrome()

'Параметризация теста с передачей в фикстуру списка с одиночными элементами'
# пример тестирования сайта в разных языковых версиях ((*) лучше исп.запуск браузера в нужной языковой версии - 8_options):
@pytest.mark.parametrize('language', ["ru", "eng", "fr"])
def test_multilanguage(language):
    link = f"https://www.selenium.dev/{language}/"      # path-параметры из списка (языков. версии) подставляются и передаются в URL
    driver.get(link)
    # /какие-то проверки/


'Параметризация теста с передачей в фикстуру списка с парными элементами'
# пример тестирования авторизации на сайте разными данными авторизации:
@pytest.mark.parametrize('creds', [('user1@mail.com', 'qwqwqw'), ('user2@mail.com', 'asasas'), ('user3@mail.com', 'zxzxzx')])
def test_login(creds):
    login, passw = creds        # запишем в переменные пары логин/пароль из кортежей (которые распаковывает кастом. параметр creds)
    # /поиск и запись в переменные веб-элементов/
    login_field.send_keys(login)
    passw_field.send_keys(passw)
    # /какие-то проверки/

# (*) Можно модифицировать наш список для большей информативности отчета:
# [
#     pytest.param(('user1@mail.com', 'qwqwqw'), id='user1@mail.com', 'qwqwqw')
#     pytest.param(('user2@mail.com', 'asasas'), id='user2@mail.com', 'asasas')
#     pytest.param(('user3@mail.com', 'zxzxzx'), id='user3@mail.com', 'xzxzx')
# ]


'Генерация списка для попарного тестирования (для залогинивания всеми возможными комбинациями из логинов и паролей)'
# 1. Вынесем в отдельные переменные списки со всеми логинами и паролями:
login = ['user1@mail.com', 'user2@mail.com', 'user3@mail.com']
passw = ['qwqwqw', 'asasas', 'zxzxzx']


# 2. Напишем функцию по генерации списка со всеми комбинациями логин-пароль:
def generate_pairs(login, passw):
    pairs = []
    for i in login:
        for j in passw:
            pairs.append((login, passw))
            # pairs.append(pytest.param((login, passw), id=f'{login}, {passw}'))   # модиф. вариант для большей информативности отчета
    return pairs


# 3. В параметры фикстуры вместо готового списка с данными передадим нашу функцию генерирующую список:
@pytest.mark.parametrize('creds', generate_pairs(login, passw))
def test_login(creds):
    login, passw = creds
    # /дальше идет поиск веб-элементов и запись их в переменные/
    login_field.send_keys(login)
    passw_field.send_keys(passw)
    # /какие-то проверки/

# (!!!) ВСЕ ТЕСТЫ НА ЭТОЙ СТРАНИЦЕ УПАДУТ, т.к. они учебные и не для запуска, т.к. не определены локаторы login_field и passw_field
