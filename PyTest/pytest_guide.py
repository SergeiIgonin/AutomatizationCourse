"""Гайд по PyTest"""

import pytest


'1. УСТАНОВКА PYTEST'
# В терминале в вирт. окружение (напр. Selenium - в пайчарме оно создается автоматически) переходим в папку с тестами,
# напр., (Selenium) PS D:\PycharmProjects\Selenium\Pytest\tests> и там пишем команду>
'pip(3) install pytest'
# для проверки установки в пайчарме перейти в: File -> Settings -> Папка проекта -> в списке ищем pytest или
# в файле с тестами (в виде функций) импортируем пайтест - он должен подставиться без подчеркиваний.


'2. ЗАПУСК ТЕСТОВ C РАЗЛИЧНЫМИ ФЛАГАМИ ЗАПУСКА'
# В файлах запустятся все функции вне классов нач. на "test_" или внутри всех классов нач. на Test (но без методов __init__ внутри)
'pytest'                                      # Базовая команда, запускает тесты во всех папках с именами test_*.py или *_test.py
'pytest -s'                                   # Выводит все принты из тестов
'pytest -v'                                   # Выводит подробный отчет
'pytest -sv'                                  # Стандартная команда для запуска тестов
'pytest -m smoke'                             # Запуск только маркированных тестов с указанием флага -m и названием метки
'pytest -m "not smoke"'                       # Инверсия запуска тестов (после флага -m в кавычках пишем название метки-исключения)
'pytest -m "smoke or regression"'             # Запуск тестов при наличии у них одной или другой метки
'pytest -m "smoke and regression"'            # Запуск тестов при наличии у них ОДНОВРЕМЕННО одной и другой метки
'pytest tests'                                # Запуск тестов из указанной папки - зависит от текущей папки нахождения (cd / cd..)
'pytest tests\test_3_marks.py.py'             # Запуск тестов из указанного файла
'pytest tests\test_3_marks.py::test_1'        # Запуск указанного теста из указанного файла
'pytest --tb=line'                            # Запуск теста с сокращенным логом отчета
'pytest --language=en'                        # Запуск теста в англ. яз. версии браузера*
'pytest --browser_name=firefox'               # Запуск теста в браузере firefox*
# (*) см. ссылку по соответствующим настройкам в conftest.py: https://stepik.org/lesson/237240/step/7?unit=209628
'pytest -m "smoke or regression" --tb=line --browser_name=firefox PyTest\tests\test_3_marks.py.py::test_1' # пример составной команды


'3. ФИКСАЦИЯ ВСЕХ УСТАНОВЛЕННЫХ ДЛЯ ТЕКУЩЕГО ВИРТ.ОКР. МОДУЛЕЙ В ФАЙЛ requirements.txt (после установки всех необходимых модулей)'
'pip freeze > requirements.txt'    # команда создаст файл requirements.txt и сохранит в него все версии пакетов используемых тек. окр.
'pip install -r requirements.txt'  # команда установки всех модулей в свежем вирт.окр. (после его создания) одной командой.


'4. ФИКСТУРЫ, ОПЕРАТОР YIELD, ОБЛАСТЬ ПОКРЫТИЯ SCOPE. АВТОИСПОЛЬЗОВАНИЕ ФИКСТУР'
# Фикстура это спец. функция служащая для выполнения определенных предусловий и постусловий при запуске тестов.
# От функций с тестами фикстуры отличаются наличием спец. декоратора - @pytest.fixture()
# Оператор yield в фикстурах разделяет предусловия от постусловий (все, что выше него - предусловия, все что ниже - постусловия)
# Для фикстур можно задавать область их покрытия в параметре scope. Допустимые значения: “function”, “class”, “module”, “session”.
# (!) параметр scope указывается в декораторе, а не в самой функции с кодом.
# Пример фикстуры:
@pytest.fixture(scope="session")   # после подкл. к тесту отработает предусловие из фикстуры, а в конце сессии пайтеста -постусловие
def separator():
    print('=' * 10)                # предусловие
    yield                          # yield == return - может что-то возвращать, если нужно
    print('Проверки закончены')    # постусловие

'Автоиспользование фикстуры'
@pytest.fixture(autouse=True)
# Имя фикстуры с таким параметром не нужно передавать в параметры тестовых функций, т.к. она будет использована автоматически.


'5. МАРКИРОВКА ТЕСТОВ'
# Имеет вид декораторов над тестовыми функциями или тестовыми классами.
# Если для одной тестовой функции нужно поставить несколько маркировок, то пишем их друг под другом с новой строки.
'Пропуск тестов'
@pytest.mark.skip("Баг до сих пор не пофикшен")             # в скобках можно указать причину пропуска
'Маркировка тестов, как ожидаемо падающих (XFAIL)'
@pytest.mark.xfail(reason="Баг до сих пор не пофикшен")     # в скобках можно указать причину падения
'Кастомная маркировка'
# см. примечание ниже (*)
@pytest.mark.smoke
@pytest.mark.regression
'Очередность запуска тестов'
# (!) Предварительно нужно установить спец. модуль> pip(3) install pytest-ordering
@pytest.mark.run(order=1)
@pytest.mark.run(order=2)
@pytest.mark.run(order=3)
'Обход WARNINGS при запуске тестов с кастомными метками (файл pytest.ini)'
# (*) Т.к. системе неизвестны наши кастомные метки, то из-за них после запуска тестов будут приходить warnings.
# Для их отключения в корне проекта нужно создать файл pytest.ini, в котором прописать все наши кастомные маркировки.
# Образец структуры файла тут: https://docs.pytest.org/en/stable/how-to/mark.html
# Или же warnings можно отключить в терминале командой --disable-warnings (не рекомендуется)


'6. СОХРАНЕНИЕ ВСЕХ ФИКСТУР В ФАЙЛ conftest.py'
# (!) Создать файл conftest.py параллельно папке tests и поместить в него все необходимые фикстуры.
# (*) Ссылка с инфой о том, что нужно прописать в conftest.py чтобы можно было запускать все тесты только в хроме или только
# в файрфоксе, в разных языковых версиях сайта, с указанием названия браузера и/или языка в самой команде pytest:
# https://stepik.org/lesson/237240/step/7?unit=209628


'7. ПАРАМЕТРИЗАЦИЯ ТЕСТОВ (ДИНАМИЧЕСКИЕ ФИКСТУРЫ)'
# Для одного теста можно задать разные параметры — тест запустится несколько раз с разными тестовыми данными.
# В фикстуру сначала передаем кастом. параметр (который затем вместо себя будет подставлять значения из списка), затем сам список.
# Пример парам. фикстуры со списком из одиночных элем.:
@pytest.mark.parametrize('language', ["ru", "eng"])
# Пример парам. фикстуры со списком из парных элем. (внутри списка кортежи с парами логин/пароль):
@pytest.mark.parametrize('creds', [("user1@mail.ru", "123"), ("user2@mail.ru", "456")])
# Данные из списка будут распаковываться, перебираться и подставляться при передачи кастом. параметра в тестовую функцию.
# Если элем. внутри списка парные и обернуты в кортежи, то после определения тестовой функции их нужно вынести в переменную.
# Например, так: login, passw = creds
# Т.о. кастом. параметр creds распакует из списка все кортежи с парами логин/пароль и подставит их в переменные login и passw.


'8. ПЕРЕЗАПУСК УПАВШИХ ТЕСТОВ'
# Нестабильные "мигающие" авто-тесты желательно перезапускать в случае падения, чтобы понять баг это или случайность.
# Для этого  установим плагин в нашем вирт. окружении>
'pip install pytest-rerunfailures'
# Теперь упавшие тесты можно запускать такой командой>
'pytest -v -s --tb=line --reruns 2 PyTest\Tests\Test_1_fixture,yield.py'
# "--tb=line"  флаг служит для сокращения лога отчета;
# "--reruns n" флаг перезапуска упавших тестов, где n — это количество перезапусков.