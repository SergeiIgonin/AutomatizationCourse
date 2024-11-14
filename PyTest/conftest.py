"""Пример содержимого папки conftest.py"""

# (!) файл conftest.py должен лежать параллельно папке tests
import pytest


@pytest.fixture()                           # первая фикстура
def start_and_fin():
    print(' Предусловие теста с фикстурой')
    yield
    print(' Постусловие теста с фикстурой')


@pytest.fixture()                           # вторая фикстура
def separator():
    print('-' * 100)


# фикстур может быть сколько угодно ещё
