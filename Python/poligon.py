# print(list(range(1,5)))
#
# date = input('Введите год вашего рождения: ')
# print(f'Год вашего рождения {date} год')
#
# def give_age(current_year):
#     self_age = int(current_year) - int(date)
#     print(f'Ваш возраст {self_age} лет')
#
# give_age(2050)

#
# def func(x):
#     if x % 2 == 0:
#         print('Это четное число')
#     else:
#         print('Это нечетное число')
#
# func(22)
# sp1 = [1,2,3,4,5]
# sp2 = [6,7,8,9,10]
# sp3 = sp1+sp2
# print(sp3)
# print()

# x = 'абырвалг'
# print(x[::-1])

# print(4 % 2)

# s = 'hello world'
# sl = set(s)
# print(sl)

# sp = []
# sp.append('hello')
# print(sp)


# print(sum(i for i in range(0, 11, 5)))      # 5 + 10 = 15

print('Пример простой функции принимающей в качестве параметров пользовательский ввод')

print('Введите первое число: ')
n1 = int(input())
print('Введите второе число: ')
n2 = int(input())


def fun5(a, b):
    return a * b


print(f'Произведение двух чисел равно {fun5(n1, n2)}')
