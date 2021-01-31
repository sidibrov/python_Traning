# -*- coding: utf-8 -*-
import simple_draw as sd
import random as random


# (определение функций)

def smile(x=100, y=100, color=sd.COLOR_DARK_ORANGE):
    """

    :rtype: object
    """
    left_bottom = sd.get_point(x - 50, y - 40)
    right_top = sd.get_point(x + 50, y + 40)
    sd.ellipse(left_bottom, right_top, color, width=2)
    sd.circle(center_position=sd.get_point(x - 15, y + 15), radius=5, color=sd.COLOR_DARK_ORANGE, width=2)
    sd.circle(center_position=sd.get_point(x + 15, y + 15), radius=5, color=sd.COLOR_DARK_ORANGE, width=2)
    point_list = [sd.get_point(x - 15, y - 10),
                  sd.get_point(x - 5, y - 20),
                  sd.get_point(x + 5, y - 20),
                  sd.get_point(x + 15, y - 10)
                  ]
    sd.lines(point_list, color=sd.COLOR_DARK_ORANGE, closed=False, width=2)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
for _ in range(10):
    point = sd.random_point()
    smile(x=random.randint(50, 550), y=random.randint(50, 550), color=sd.COLOR_DARK_ORANGE)

sd.pause()
