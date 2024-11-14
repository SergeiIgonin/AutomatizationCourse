"Типы данных Python"

x = 25
print(type(x))

y = 10.33
print(type(y))

z = 'qwe"R"ty'
print(type(z))

bulean = 'True/False'
# True эквивалентно 1, False эквивалентно 0
x = 2000000 == 2_000_000
y = 1 > 10
print(x, y)
print('ll' in 'hello')
print(type("abc") is str)
print(type(123) is not str)


print('Математические действия')
a = 5 + 5
b = 8 - 2
c = 3 * 3
print(a, b, c)

print('Возведение в степень')
a = 3 ** 3
print(a)

print('Деление')   # всегда возвращает вещественное число
a = 12 / 5
print(a)

print('Деление без остатка')
a = 12 // 5
print(a)

print('Остаток от деления')
a = 10 % 3
print(a)

print('Округление')
x = 20
y = 6
print(round(x / y))

print('Сумма элементов')
a = [3, 2, 4, 1]
print(sum(a))

a = sum([10, 15])
print(a)




