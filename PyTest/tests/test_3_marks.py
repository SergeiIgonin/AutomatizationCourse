"""Маркировка тестов"""
import pytest


'Пропуск тестов'
@pytest.mark.skip("Баг до сих пор не пофикшен")             # в скобках можно указать причину пропуска
def test_1():
    assert 1 == 2, 'something is wrong'


'Маркировка тестов, как ожидаемо падающих (XFAIL)'
@pytest.mark.xfail(reason="Баг до сих пор не пофикшен")     # сообщение с причиной падения добавлять не обязательно
def test_2():
    assert 1 == 2, 'something is wrong'
# (!) Теперь после прохождения проверок тест с такой меткой будет помечен как XFAIL, но когда баг починят отметка сменится на XPASS.
# Чтобы увидеть в отчете pytest сообщение с причиной падения нужно добавить флаг -rx к команде pytest:
# pytest -v -s -rx PyTest\tests\test_3_marks.py


'Произвольная маркировка тестов (кастомные метки)'
# Наши кастомные метки предварительно нужно внести в созданный в корне папки проекта файл pytest.ini
# Образец структуры файла тут: https://docs.pytest.org/en/stable/how-to/mark.html (описание меток можно добавлять по желанию)


@pytest.mark.smoke                          # тест маркированный одной меткой
def test_3():
    assert 2 == 2, 'something is wrong'


@pytest.mark.smoke                          # тест маркированный сразу двумя метками
@pytest.mark.regression
def test_4():
    assert 3 == 3, 'something is wrong'


'Команды для выборочного запуска маркированных тестов'
# pytest -v -s -m smoke                     запустятся все тесты с указанной меткой
# pytest -v -s -m "not smoke"               запустятся все тесты не помеченные указанной меткой (инверсия)
# pytest -s -v -m "smoke or regression"     запустятся все тесты у которых есть хотябы одна из указанных меток
# pytest -s -v -m "smoke and regression"    запустятся все тесты у которых есть одновременно обе указанные метки


'Настройка очередности запуска тестов (нумерация тестов)'
# (!) Предварительно нужно установить спец. модуль>
'pip(3) install pytest-ordering'
@pytest.mark.run(order=1)
def test_5():
    print('- тест маркирован 1м по запуску')
    assert 4 == 4, 'something is wrong'

@pytest.mark.run(order=2)
def test_6():
    print('- тест маркирован 2м по запуску')
    assert 5 == 5, 'something is wrong'

@pytest.mark.run(order=3)
def test_7():
    print(' - тест маркирован 3м по запуску')
    assert 5 == 5, 'something is wrong'
