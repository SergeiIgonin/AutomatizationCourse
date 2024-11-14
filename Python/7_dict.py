"""Словарь {a:b} это изменяемая, неупорядоченная структура/модель данных, хранящая пары 'ключ' : 'значение'.
У элементов нет индекса, вместо них ключи"""

print('\nСоздание пустого словаря двумя способами')
sl = {}
print(sl)

sl = dict()
print(sl)

print('Создание заполненного парными элементами словаря')
sl = {
    1: 'one',
    2: 'two',
    3: 'three'
}
print(sl)

print('Создания словаря генератором с желаемым условием')
sl = {i: i*2 for i in range(1, 6)}
print(sl)

print('Создания словаря генератором на основе строки (хотим узнать сколько раз каждый символ встречается в строке)')
s = 'hello world'
sl = {i: s.count(i) for i in set(s)}
print(sl)

print('Cоздание словаря на основе двух списков, при условии одинакового кол-ва эл. в них')
sp1 = [1, 2, 3]
sp2 = ['one', 'two', 'three']
sl = dict(zip(sp1, sp2))
print(sl)

#########################################################
print('\n МЕТОДЫ РАБОТЫ СО СЛОВАРЯМИ:\n')

print('Проверить наличия ключа в словаре')
sl = {'Alex': 25, 'Pavel': 37, 'Kate': 19}
print('Kate' in sl)

print('Вывести значение по ключу')
sl = {'Alex': 32, 'Kate': 19}
print(sl['Kate'])

print('Изменить значение по ключу')
sl = {'Alex': 32, 'Pavel': 36}
sl['Pavel'] = 37
print(sl)

print('Добавить новую пару')
sl = {'Alex': 32, 'Pavel': 37}
sl['Kate'] = 19
print(sl)

print('Удалить пару по ключу (pop)')
sl = {'Alex': 25, 'Pavel': 37, 'Kate': 19}
sl.pop('Alex')
print(sl)

print('Удалить пару из словаря с предв. проверкой ее наличия (del)')
sl = {'Alex': 25, 'Pavel': 37, 'Kate': 19}
if 'Pavel' in sl:                   # или not in - проверка отсутствия наличия
    del sl['Pavel']
print(sl)

print('Очистить словарь от всех элементов (clear)')
sl = {'Alex': 25, 'Pavel': 37, 'Kate': 19}
sl.clear()
print(sl)

print('Вывести все ключи')
sl = {'Alex': 25, 'Pavel': 37, 'Kate': 19}
for k in sl.keys():
    print(f'Ключ: {k}')

print('Вывести все значения')
sl = {'Alex': 25, 'Pavel': 37, 'Kate': 19}
for v in sl.values():
    print(f'Значение: {v}')

print('Вывести все ключи и значения')
sl = {'Alex': 25, 'Pavel': 37, 'Kate': 19}
for k, v in sl.items():
    print(f'Ключ: {k}, значение: {v}')

print('Вывести значение из вложенного словаря')
sl = {
    'Lea': {
        'phone': 88125555555,
        'address': 'St.Petersburg'
    },
    'Max': {
        'phone': 84956666666,
        'address': 'Moscow'
    }
}
print(sl['Lea']['address'])

print('Вывести длину словаря (кол-во всех пар в нем)')
sl = {'Alex': 25, 'Pavel': 37, 'Kate': 19}
print(len(sl))
