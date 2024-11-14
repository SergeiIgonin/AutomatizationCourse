'Работа с файлами (создание файла, запись и перезапись в файл, чтение из файла, удаление файла)'
'В txt-файлы можно записывать только строковый тип данных'


# Можно создать в проекте отдельную папку в которой будем создавать файл (напр., /doc)
# флаг "w" (write) = запись и перезапись данных с удалением предыдущих данных
# флаг "a" (append) = дозапись данных в файл с добавлением нового текста после старого
# флаг "r" (read) = чтение из файла (вывод текста в консоль)


'Запись/перезапись данных в txt-файл (если файл не существует он создается)'
f = open('my_file.txt', 'w')    # если txt-файл и текущий py-файл в одной папке, то можно указать только имя файла
f.write('Hello!')
f.close()

# 'Дозапись в txt-файл с помещением в него введенного текста (input)'
# new_text = input("Введите текст на латинице: ")
# f = open('my_file.txt', 'a')
# f.write(new_text)
# f.close

'Чтение из txt-файла'
f = open('my_file.txt', 'r')
print(f.read())
# print(*f)                     # альтернативный способ чтения из файла с пом. распаковщика
f.close()


#####################
'КОНТЕКСТНЫЙ МЕНЕДЖЕР "WITH" для автоматического закрытия файла после действий с ним'
with open('my_file1.txt', 'w') as f1:
    f1.write('Hi dude.\n')       # \n = новый текст будет с новой строки

with open('my_file1.txt', 'a') as f1:
    f1.write('You are the best!')

with open('my_file1.txt', 'r') as f1:
    print(f1.read())

'Проверка закрыт ли в данный момент файл или нет'
print(f1.closed)         # возвращает булево значение


'Для проверки существования файла в Python есть встроенные функции os.path.isfile() или os.path.exists()'
import os

filename = 'my_file1.txt'

if os.path.exists(filename):
    print("Файл существует")
else:
    print("Файл не существует")

# 'Удаление файла, если он существует'
# if os.path.exists(filename):
#     os.remove(filename)
#
# 'Повторная проверка после удаления файла'
# if os.path.exists(filename):
#     print("Файл существует")
# else:
#     print("Файл не существует")