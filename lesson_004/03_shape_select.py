# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def triangle(start_point, angle, color, length):
    any_figure(number_of_sides=3, start_point=start_point, angle=angle, length=length, color=color, width=3)


def square(start_point, angle, color, length):
    any_figure(number_of_sides=4, start_point=start_point, angle=angle, length=length, color=color, width=3)


def pentagon(start_point, angle, color, length):
    any_figure(number_of_sides=5, start_point=start_point, angle=angle, length=length, color=color, width=3)


def hexagon(start_point, angle, color, length):
    any_figure(number_of_sides=6, start_point=start_point, angle=angle, length=length, color=color, width=3)


def any_figure(number_of_sides, start_point, angle, length, color, width):
    sides = []
    sides.append(sd.get_vector(start_point=start_point, angle=angle, length=length))
    sides[0].draw(color=color, width=width)
    for i in range(1, number_of_sides, 1):
        sides.append(sd.get_vector(start_point=sides[i - 1].end_point, angle=angle + 360 * i / number_of_sides,
                                   length=length, width=3))
        sides[i].draw(color=color, width=width)
    sd.line(start_point=start_point, end_point=sides[len(sides) - 1].end_point, color=color, width=width)


choice = ''
mistake = True
while mistake:
    print("Please, choose figure:")
    print('1 - triangle')
    print('2 - square')
    print('3 - pentagon')
    print('4 - hexagon')
    print('q - quit')
    choice = input('Your choice is : ')
    if choice == "1":
        triangle(start_point=sd.get_point(x=300, y=250), angle=80, color=sd.COLOR_YELLOW, length=150)
        mistake = False
    elif choice == "2":
        square(start_point=sd.get_point(x=300, y=250), angle=60, color=sd.COLOR_YELLOW, length=125)
        mistake = False
    elif choice == "3":
        pentagon(start_point=sd.get_point(x=300, y=250), angle=60, color=sd.COLOR_YELLOW, length=100)
        mistake = False
    elif choice == "4":
        hexagon(start_point=sd.get_point(x=300, y=250), angle=40, color=sd.COLOR_YELLOW, length=90)
        mistake = False
    elif choice == "q":
        choice = None
        break
    else:
        print("Incorrect choice")
        choice = None
if choice:
    sd.pause()
