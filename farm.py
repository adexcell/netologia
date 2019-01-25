import time
print(time.strftime("%H:%M:%S"))
now = time.localtime()

print('''    Здравствуй, дорогой племянник "%username%"! Спасибо, что согласился приехать помочь мне с хозяйством, 
    пока я буду в отъезде. К сожалению, не успеваю тебя встретить, и оставляю эту инструкцию. 
    Не сомневаюсь, ты справишься!
    _____________________________''')
# Домашнее задание к лекции «Классы и их применение в Python»
class Animal:
    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice

    # Описываем общие методы взаимодействия: кормление, голос, продукт
    def names(self):
        # Животные на ферме, которых нужно кормить
        print("  {} ".format(self.name))

    def voice(self):
        # различать по голосам
        pass

    def product(self):
        # Продукт, который получает дядюшка от животных на ферме от стрижки, дойки, сбора яиц
        pass

# Класс для овец
class Sheep(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'бе-бе-бе')

    # Метод shear(стрич)
    def shear(self):
        # овец стричь(shear)
        print("  шерсть от {}".format(self.name))

    # Переопределение метода для вызова метода shear
    def product(self):
        self.shear()


# Общий класс для коров и коз, в которм будет создан метод milk
# Класс является потомком Animal: наследуются параметры, методы(feed, voice)
class MilkAnimal(Animal):
    def milk(self):
        # корову и коз доить
        print("  молоко от {}".format(self.name))

    def product(self):
        self.milk()


# Классы для коров и коз. Наследуем методы от родителя MilkAnimal и Animal
class Cow(MilkAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'мууу')


class Goat(MilkAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'ме-ме-ме')


# Общий класс для птиц.
# Класс является потомком Animal. Наследуются параметры, методы(feed, voice)
# Добавлен метод - egg и переопределен метод product для запуска egg
class Bird(Animal):
    def egg(self):
        # собирать яйца у кур, уток и гусей
        print("  яйца от {}".format(self.name))

    def product(self):
        self.egg()


# Классы для гусей, кур и уток. Наследуем методы от родителя Bird и Animal
class Goose(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'га-га-га')


class Chicken(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'кудахчет')


class Duck(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'кря-кря-кря')



# Для каждого животного из списка должен существовать экземпляр класса.
goose1 = Goose('Гусыня "Серая"', 3.3)
goose2 = Goose('Гусыня "Белая"', 2.5)
cow = Cow('Корова "Манька"', 430)
sheep1 = Sheep('Овечка "Барашек"', 75)
sheep2 = Sheep('Овечка "Кудрявая"', 56)
goat1 = Goat('Коза "Рога"', 25)
goat2 = Goat('Коза "Копыта"', 27)
chicken1 = Chicken('Курица "Ko-Ko"', 2.5)
chicken2 = Chicken('Курица "Кукареку"', 3.2)
duck = Duck('Утка "Кряква"', 4.5)

animals = [goose1, goose2, cow, sheep1, sheep2, chicken1, chicken2, goat1, goat2, duck]

print('\n Все мои животные:')
for animal in animals:
    print('  {} издаёт звук "{}" '.format(animal.name, animal.voice))

print('\n Что дают мои животные:')
for animal in animals:
    animal.product()

print('\n Животных кормить дважды в день! с 6 до 8 утра, и с 18 до 20 вечера.')
print("Сейчас:", time.strftime("%H:%M"))
if 6<now.tm_hour<8 or 18<now.tm_hour<20:
    print(' \nПокорми моих животных: ')
    for animal in animals:
        animal.names()
else:
    print("Время кормить еще не пришло")

# Вывести животных, которых соответственно требуется подоить/постричь/собрать яйца



total_weight = 0
# heaviest_animal = None
for animal in animals:
    total_weight = total_weight + animal.weight
print('\nОбщий вес всех животных: ', format(total_weight))

heaviest_animal = None
for animal in animals:
    if heaviest_animal is None:
        heaviest_animal = animal
    elif animal.weight > heaviest_animal.weight:
        heaviest_animal = animal
print('Самое тяжёлое животное: {}, имеет вес: {} кг, издаёт звук: {} '.format(heaviest_animal.name,
                                                                              heaviest_animal.weight,
                                                                              heaviest_animal.voice))