# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

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


color = ''
mistake = True
while mistake:
    print("Please, choose color:")
    print('1 - RED')
    print('2 - ORANGE')
    print('3 - YELLOW')
    print('4 - GREEN')
    print('5 - CYAN')
    print('6 - BLUE')
    print('7 - PURPLE')
    print('q - quit')
    color = input('Your choice is : ')
    if color == "1":
        color = sd.COLOR_RED
        mistake = False
    elif color == "2":
        color = sd.COLOR_ORANGE
        mistake = False
    elif color == "3":
        color = sd.COLOR_YELLOW
        mistake = False
    elif color == "4":
        color = sd.COLOR_GREEN
        mistake = False
    elif color == "5":
        color = sd.COLOR_CYAN
        mistake = False
    elif color == "6":
        color = sd.COLOR_BLUE
        mistake = False
    elif color == "7":
        color = sd.COLOR_PURPLE
        mistake = False
    elif color == "q":
        color = None
        break
    else:
        print("Incorrect choice")
        color = None
if color:
    triangle(start_point=sd.get_point(x=200, y=400), angle=80, color=color, length=150)
    square(start_point=sd.get_point(x=450, y=375), angle=60, color=color, length=125)
    pentagon(start_point=sd.get_point(x=200, y=100), angle=60, color=color, length=100)
    hexagon(start_point=sd.get_point(x=450, y=100), angle=40, color=color, length=90)
    sd.pause()
