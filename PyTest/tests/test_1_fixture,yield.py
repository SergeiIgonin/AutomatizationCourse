"""Использование фикстур. Оператор yield"""
# Для запуска тестов сам файл c тестами и функции в нем должны именоваться test_*.py или *_test.py
import pytest


@pytest.fixture()                        # фикстура 1
def start_and_fin():
    print(' Предусловие теста с фикстурой')
    yield                                # yield == return - может что-то возвращать, если нужно
    print(' Постусловие теста с фикстурой')


@pytest.fixture()                        # фикстура 2
def separator():
    print('-' * 100)


def test_one(start_and_fin, separator):  # пример теста с использованием обеих фикстур (их указываем в параметрах)
    assert 1 == 1, 'something is wrong'


def test_two(start_and_fin, separator):  # пример падающего теста с использованием обеих фикстур
    assert 2 == 3, 'Ожидаемое падение теста (для демонстрации)'


def test_three(start_and_fin):           # пример теста с использованием только одной фикстуры
    assert 3 == 3, 'something is wrong'


'Автоиспользование фикстуры'
# @pytest.fixture(autouse=True)
# Имя фикстуры с таким параметром не нужно передавать в параметры тестовых функций, т.к. она будет использована автоматически.
