'Наследование, полиморфизм, инкапсуляция'


class Race:                     # создание род.класса 1
    def __init__(self, race):
        self.race = race

    def battle_cry(self):       # создание метода класса
        # print('WAAAAGH!!!') if self.race == 'orc' else print ('Lok-Tar Ogar!') — пример исп. тернарного оператора
        if self.race == 'orc':
            print('WAAAAGH!!!')
        elif self.race == 'human':
            print('URAAA!!!')
        else:
            print('Lok-Tar Ogar!!!')

# dweller_1 = Race('elf')       # создание объекта класса "Race"
# dweller_1.battle_cry()        # вызов метода "battle_cry" на объекте


class Forces:                  # создание род.класса 2 (параллельного по иерархии с первым)
    def __init__(self, specializing):
        self.specializing = specializing

    def scary_movement(self):   # создание метода класса
        # print('swings spear') if self.specializing == 'spearman' else print ('draws bow') — тернарный оператор(пример)
        if self.specializing == 'swordsman':
            print('taps sword on shield')
        elif self.specializing == 'spearman':
            print('swings spear')
        else:
            print('draws bow')


class Knights(Forces):                  # создание субкласса на основе род.класса 1
    knight_count = 0

    def __init__(self, specializing, armor, speed):   # в конструкторе указываются атрибуты род.класса и собственные атрибуты (субкласса)
        super().__init__(specializing)                # наследование атрибутов род.класса "Classes"
        self.armor = armor              # добавление уник. атрибутов или переопределение родительских
        self.speed = speed
        self.stamina = 250              # атрибут с предопределенным значением (не добавляется в параметры конструктора)
        Knights.knight_count += 1
        print(f'A knight № {self.knight_count} joins your army, milord!')


k_1 = Knights('swordsman', 'closed armor', 200)  # создание объекта субкласса

print(k_1.armor, k_1.specializing)      # вызов на объекте субкласса атрибутов и субкласса и род.класса
k_1.scary_movement()                    # вызов на объекте субкласса метода род.класса


class Warrior(Forces, Race):                            # создание субкласса на основе одновременно двух род.классов
    def __init__(self, name, age, race, specializing, rank):
        Race.__init__(self, race)                       # наследование атрибутов род.класса 1
        Forces.__init__(self, specializing)             # наследование атрибутов род.класса 2
        self.name = name                                # добавление уникальных атрибутов
        self.age = age
        self.rank = rank

    def __str__(self):                                  # дает описание объекта при его вызове в виде переменной
        return f'Name: {self.name}, Age: {self.age}, Race: {self.race}, Class: {self.specializing}, Rank: {self.rank}'


w_1 = Warrior('Gorgutz',45,'orc','spearman','general')
w_2 = Warrior('noname',116,'elf','archer','private soldier')
w_3 = Warrior('Darius',28,'human','swordsman','captain')

print(w_1)              # вызов метода описания объекта (def __str__(self):)
w_1.battle_cry()
w_1.scary_movement()

print(w_2)
w_2.battle_cry()
w_2.scary_movement()

print(w_3)
w_3.battle_cry()
w_3.scary_movement()

#########################################
print('ПОЛИМОРФИЗМ - обращение к объектам разных классов, как к объектам одного класса')
for warrior in (w_1, w_2, w_3, k_1):              # также можно обратиться к списку или к множеству с разными объектами
    warrior.scary_movement()                      # желательно чтобы у всех классов были одинаковые названия методов

#########################################
print('ИНКАПСУЛЯЦИЯ (конструкция "self.__x = x")')


class Person:

    def __init__(self, name, age):
        self.name = name                # публичный атрибут
        self.__age = age                # приватный атрибут

    def get_age(self):                  # метод геттер (для получения значения приватного атрибута объекта)
        return self.__age

    def set_age(self, age):             # метод сеттер (для перезаписи значения приватного атрибута объекта)
        self.__age = age


p1 = Person('Lea', 35)       # создание объекта класса Person с приватным атрибутом "age" (как по конструктору)

print(p1.name)                          # получение значения публичного атрибута объекта
# print(p1.age)                         # получить значение приватного атрибута так нельзя
print(p1.get_age())                     # получение значения приватного атрибута ТОЛЬКО через метод-геттер

p1.name = 'Liya'                        # перезапись значения публичного атрибута объекта
# p1.age = 36                           # перезаписать значение приватного атрибута так нельзя
p1.set_age(36)                          # перезапись значения приватного атрибута ТОЛЬКО через метод-сеттер

print(p1.name)                          # проверка изменений после перезаписи значения публичного атрибута
print(p1.get_age())                     # проверка изменений после перезаписи значения приватного атрибута
