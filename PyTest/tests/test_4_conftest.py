"""Тестовый файл, который обращается к фикстурам из файла pytest.py"""
# В корне проекта, а лучше в корневой папке в которой находятся папки с тестовыми файлами создать файл conftest.py,
# в котором написать 'import pytest' и ниже поместить все необходимые фикстуры.
# При создании тестовых функций просто передавать в их атрибуты нужные фикстуры — они подтянутся автоматически.


def test_my(separator):
    print("Hello dude!:)")
    assert 1 == 1, "Something is wrong"