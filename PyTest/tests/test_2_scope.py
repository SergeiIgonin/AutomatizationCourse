"""Настройка области покрытия фикстуры — параметр scope"""
# по умолчанию scope="function". Допустимые значения: "function", "class", "module", "session".
import pytest


@pytest.fixture(scope='module')     # указываем область покрытия фикстуры (module = текущий файл)
def db_connect():
    print(' Подключение к БД (Тесты со скоупом)')
    yield
    print(' Отключение от БД (Тесты со скоупом)')


def test_1():
    assert 1 == 1, 'something is wrong'


def test_2(db_connect):           # начиная с этого теста мы задействуем фикстуру (т.е. выполняется предусловие - подключение к БД)
    assert 2 == 2, 'something is wrong'


def test_3():
    assert 3 == 3, 'something is wrong'


def test_4():
    assert 4 == 4, 'something is wrong'


def test_5():
    assert 5 == 5, 'something is wrong'

# после окончания тестов в этом файле мы отключаемся от БД (согласно постусловию после yield)
