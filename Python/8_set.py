"""Множество {a,b,c} это изменяемая, неупорядоченная структура/модель данных, состоящая из уникальных элементов.
Элементы множества не имеют индекса (т.е. множество это своеобразный 'мешок')"""

print('\nСоздание словаря, а не множества')
sl = {}
print(type(sl))

print('Создание пустого множества и множества с элементами')
mn = set()
mn = {'hello', 10.5, 25, 'hello', 25, 10.5}     # все дубли удаляются
print(mn)

print('Создание множества на основе списка и наоборот — когда хотим убрать все дубликаты из списка)')
sp = [1, 3, 1, 2, 1, 2, 3, 3, 2]
mn = set(sp)
sp = list(mn)
print(sp)

print('Создание множества генератором на основе диапазона чисел')
mn = {i for i in range(1,10)}
print(mn)


print('\n МЕТОДЫ РАБОТЫ С МНОЖЕСТВАМИ:\n')

print('Проверка наличия элемента в множестве (отлично подходит множествам и плохо спискам)')
mn = {'hello', 10.5, 25, 'hello', 25, 10.5}
print('hello' in mn)                         # моментальный ответ из-за хэширования, т.к. нет перебора элементов

print('Проверка отсутствия элемента в множестве')
mn = {'hello', 10.5, 25, 'hello', 25, 10.5}
print('home' not in mn)

print('Добавление элемента в множество')
mn = set()
mn.add('hello')
print(mn)

print('Удаление элемента из множества')
mn = {'hello', 12}
mn.remove('hello')
print(mn)

print('Удаление первого элемента')
mn = {1, 2, 3}
mn.pop()
print(mn)

print('Сложение множеств')
mn1 = {1, 2, 3}
mn2 = {2, 3, 4}
mn3 = mn1 | mn2
print(mn3)

print('Сложение альтернативным способом')
mn1 = {1, 2, 3}
mn2 = {2, 3, 4}
mn1 |= mn2
print(mn1)

print('Вывести общие элементы (по которым множества пересекаются)')
a = {1, 2, 3}
b = {2, 3, 4}
c = a & b
print(c)

print('Вывести уникальные элементы (по которым множества не пересекаются)')
a = {1, 2, 3}
b = {2, 3, 4}
c = a ^ b
print(c)

print('Итерация по множеству')
a = {1, 2, 3}
for i in a:
    print(i)

print('Задача. Убрать все дубли и вывести сумму всех уникальных значений списка')
sp = [1, 3, 1, 2, 1, 2, 3, 3, 2]
print(sum(set(sp)))


# print('Создание замороженного, неизменяемого множества — лишнее, но на всякий случай')
# mn = {1, 2, 3}
# mn_froz = frozenset(mn)
# # mn_froz.add(12)           # при попытке добавления нового элемента выдаст ошибку
# print(mn_froz)