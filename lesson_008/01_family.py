# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint, randrange


####################################################### Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.mud = 0
        self.quantity_of_fur_coats = 0
        self.quantity_of_eaten_food = 0
        self.quantity_of_earned_money = 0
        self.food_for_cat = 50

    def __str__(self):
        tmp = f'Еды в доме -  {self.food}, денег в доме - {self.money}, корма для котов -  {self.food_for_cat},' \
              f' грязи в доме - {self.mud}'
        self.mud += 5
        return tmp

    def grand_total(self):
        return f'Всего заработано денег -  {self.quantity_of_earned_money}, еды съедено - {self.quantity_of_eaten_food}' \
               f', куплено шуб - {self.quantity_of_fur_coats} '


class Person:
    def __init__(self, name, house):
        self.fullness = 30
        self.happiness = 100
        self.name = name
        self.isalive = True
        if isinstance(house, House):
            self.house = house

    def __str__(self):
        return f'У {self.name}  сытость  - {self.fullness}, Степень счастья - {self.happiness}'

    def eat(self):
        if self.house.food >= 30:
            if self.fullness > 30:
                dice = randrange(10, 31, 10)
                self.fullness += dice
                self.house.food -= dice
                self.house.quantity_of_eaten_food += dice
            else:
                self.fullness += 30
                self.house.food -= 30
                self.house.quantity_of_eaten_food += 30
            if isinstance(self, Wife):
                cprint(f'{self.name} поела', color='yellow')
            else:
                cprint(f'{self.name} поел', color='yellow')
        else:
            self.fullness += self.house.food
            self.house.quantity_of_eaten_food += self.house.food
            self.house.food = 0
            cprint(f'                   В доме закончилась еда', color='white')

    def pat_cat(self):
        self.happiness += 5
        self.fullness -= 10
        cprint(f'{self.name} погладил(а) кота', color='yellow')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер(ла) от голода...'.format(self.name), color='red')
            self.isalive = False
            return
        if self.happiness <= 10:
            cprint('{} умер(ла) от дипрессии...'.format(self.name), color='red')
            self.isalive = False
            return


class Husband(Person):

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        if self.isalive:
            if self.house.mud > 90:
                self.happiness -= 10
            if self.fullness < 20:
                self.eat()
            elif self.happiness < 20:
                self.gaming()
            elif self.house.money < 200:
                self.work()
            else:
                dice = randint(1, 6)
                if 1 <= dice <= 3:
                    self.work()
                elif dice == 4:
                    self.eat()
                elif dice == 5:
                    self.gaming()
                elif dice == 6:
                    self.pat_cat()

    def work(self):
        self.fullness -= 10
        self.house.quantity_of_eaten_food += 10
        self.house.money += 150
        self.house.quantity_of_earned_money += 150
        cprint(f'{self.name} сходил на работу', color='yellow')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint(f'{self.name} поиграл в WoT', color='yellow')


class Wife(Person):

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        if self.isalive:
            if self.house.mud > 90:
                self.happiness -= 10
            if self.fullness < 20:
                self.eat()
            elif self.happiness < 20:
                self.buy_fur_coat()
            elif self.house.food < 100:
                self.shopping()
            elif self.house.food_for_cat < 20:
                self.buy_food_for_cat()
            else:
                dice = randint(1, 6)
                if dice == 1:
                    self.shopping()
                elif dice == 2:
                    self.eat()
                elif dice == 3:
                    self.clean_house()
                elif dice == 4:
                    self.buy_fur_coat()
                elif dice == 5:
                    self.buy_food_for_cat()
                elif dice == 6:
                    self.pat_cat()

    def shopping(self):
        if self.house.money <= 0:
            self.fullness -= 10
            cprint(f'                   У {self.name} не хватает денег на продукты', color='white')
            return
        if self.house.money >= 100:
            self.fullness -= 10
            self.house.food += 100
            self.house.money -= 100
        else:
            self.fullness -= 10
            self.house.food += self.house.money
            self.house.money = 0
            cprint(f'                   В доме закончились деньги', color='white')

        cprint(f'{self.name} сходила в магазин за продуктами', color='yellow')

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.fullness -= 10
            self.happiness += 60
            self.house.money -= 350
            self.house.quantity_of_fur_coats += 1
            cprint(f'{self.name} купила шубу', color='yellow')
            if self.house.money == 0:
                cprint(f'                   В доме закончились деньги', color='white')
        else:
            self.fullness -= 10
            cprint('                   У {} не хватает денег на шубу'.format(self.name), color='white')

    def clean_house(self):
        if self.house.mud < 100:
            self.house.mud = 0
        else:
            self.house.mud -= 100
        self.fullness -= 10
        cprint(f'{self.name} убралась в доме', color='yellow')

    def buy_food_for_cat(self):
        if self.house.money >= 50:
            self.house.food_for_cat += 50
            self.house.money -= 50
        else:
            self.house.food_for_cat += self.house.money
            self.house.money = 0
            cprint(f'                   В доме закончились деньги', color='white')
        cprint(f'{self.name} купил еды для кота', color='yellow')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов

class Cat:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.isalive = True
        if isinstance(house, House):
            self.house = house

    def __str__(self):
        return f'У кота {self.name} сытость {self.fullness}'

    def act(self):
        if self.fullness <= 0:
            cprint(f'Кот {self.name} умер...', color='red')
            self.isalive = False
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice % 2 == 0:
            self.sleep()
        else:
            self.soil()

    def eat(self):
        if self.house.food_for_cat >= 10:
            self.fullness += 20
            self.house.food_for_cat -= 10
            cprint(f'Кот {self.name} поел', color='yellow')
        else:
            self.house.food_for_cat = 0
            self.fullness = self.house.food_for_cat * 2
            cprint(f'{self.name} поел', color='yellow')
            cprint(f'В доме закончился корм для котов', color='white')

    def sleep(self):
        self.fullness -= 10
        cprint(f'Кот {self.name} поспал', color='yellow')

    def soil(self):
        self.fullness -= 10
        self.house.mud += 5
        cprint(f'Кот {self.name} подрал обои', color='yellow')


######################################################### Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Person):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.happiness = 100

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 2)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()

    def eat(self):
        self.fullness += 10
        cprint(f'{self.name}  поел', 'yellow')

    def sleep(self):
        self.fullness -= 10
        cprint(f'{self.name}  поспал', 'yellow')

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
murzik = Cat(name='Мурзик', house=home)

for day in range(366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')
cprint("=================================================", color='cyan')
cprint(home.grand_total(), color='green')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
