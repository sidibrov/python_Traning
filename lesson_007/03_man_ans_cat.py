# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код

class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return f'Я - {self.name}, сытость {self.fullness}'

    def sleep(self):
        self.fullness -= 10
        cprint(f'Кот {self.name} поспал', color='yellow')

    def eat(self):
        if self.house.food_for_cat >= 10:
            self.fullness += 20
            self.house.food_for_cat -= 10
            cprint(f'{self.name} поел', color='yellow')
        else:
            self.house.food_for_cat = 0
            self.fullness = self.house.food_for_cat * 2
            cprint(f'У {self.name} нет еды', color='red')

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.mud += 5
        cprint(f'Кот {self.name} подрал обои', color='yellow')

    def act(self):
        if self.fullness <= 0:
            cprint(f'Кот {self.name} умер...', color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice % 2 == 0:
            self.sleep()
        else:
            self.tear_wallpaper()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.house.money < 10:
            self.work()
        elif self.fullness < 20:
            self.eat()
        elif self.house.food < 50:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.food_for_cat < 90:
            self.buy_food_for_cat()
        elif self.house.mud > 300:
            self.tide_up_in_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            if self.house.mud > 50:
                self.tide_up_in_house()
            else:
                self.watch_MTV()
        else:
            self.watch_MTV()

    def pickup_cat(self, cat):
        if isinstance(cat, Cat):
            cat.house = self.house
            self.house.food_for_cat = 0
            self.house.mud = 0
        cprint(f'{self.name} подобрал кота', color='yellow')

    def buy_food_for_cat(self):
        self.house.food_for_cat += 100
        self.house.money -= 100
        cprint(f'{self.name} купил еды для кота', color='magenta')

    def tide_up_in_house(self):
        if self.house.mud < 100:
            self.house.mud = 0
        else:
            self.house.mud -= 100
        self.fullness -= 20
        cprint(f'{self.name} Убрался в доме', color='yellow')


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.mud = None
        self.food_for_cat = None

    def __str__(self):
        return f'В доме еды осталось - {self.food}, денег осталось - {self.money}, грязь - {self.mud},' \
               f'еды для кота осталось - {self.food_for_cat} '


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),

]
cats = [
    Cat(name='Нурик'),
    Cat(name='Лотусик'),
    Cat(name='Барсик'),
    Cat(name='Рыжик'),
    Cat(name='Тигрик'),
    Cat(name='Царапкин'),
    Cat(name='Мяуки'),
    Cat(name='Пушистик'),
    Cat(name='Помойный'),
    Cat(name='Облезлый'),
    # Cat(name='Китти'),
    # Cat(name='Кэт')
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
for cat in cats:
    citizens[randint(0, 2)].pickup_cat(cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for cat in cats:
        cat.act()
    for citisen in citizens:
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
