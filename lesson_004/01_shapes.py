# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код
def triangle(start_point, angle, color, length):
    any_figure(number_of_sides=3, start_point = start_point, angle = angle, length = length, color=color, width = 3)
    # v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    # v1.draw()
    # v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 360 * 1 / 3, length=length, width=3)
    # v2.draw()
    # v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 360 * 2 / 3, length=length, width=3)
    # v3.draw()


def square(start_point, angle, color, length):
    any_figure(number_of_sides=4, start_point=start_point, angle=angle, length=length, color=color, width=3)
    # v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    # v1.draw()
    # v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 360 * 1 / 4, length=length, width=3)
    # v2.draw()
    # v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 360 * 2 / 4, length=length, width=3)
    # v3.draw()
    # v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 360 * 3 / 4, length=length, width=3)
    # v4.draw()


def pentagon(start_point, angle, color, length):
    any_figure(number_of_sides=5, start_point=start_point, angle=angle, length=length, color=color, width=3)
    # v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    # v1.draw()
    # v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 360 * 1 / 5, length=length, width=3)
    # v2.draw()
    # v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 360 * 2 / 5, length=length, width=3)
    # v3.draw()
    # v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 360 * 3 / 5, length=length, width=3)
    # v4.draw()
    # v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 360 * 4 / 5, length=length, width=3)
    # v5.draw()


def hexagon(start_point, angle, color, length):
    any_figure(number_of_sides=6, start_point=start_point, angle=angle, length=length, color=color, width=3)
    # v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    # v1.draw()
    # v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 360 * 1 / 6, length=length, width=3)
    # v2.draw()
    # v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 360 * 2 / 6, length=length, width=3)
    # v3.draw()
    # v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 360 * 3 / 6, length=length, width=3)
    # v4.draw()
    # v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 360 * 4 / 6, length=length, width=3)
    # v5.draw()
    # v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 360 * 5 / 6, length=length, width=3)
    # v6.draw()


def any_figure(number_of_sides, start_point, angle, length, color, width):
    sides = []
    sides.append(sd.get_vector(start_point=start_point, angle=angle, length=length))
    sides[0].draw(color=color, width=width)
    for i in range(1, number_of_sides, 1):
        sides.append(sd.get_vector(start_point=sides[i - 1].end_point, angle=angle + 360 * i / number_of_sides,
                                   length=length, width=3))
        sides[i].draw(color=color, width=width)
    sd.line(start_point=start_point, end_point=sides[len(sides) - 1].end_point, color=color, width=width)


triangle(start_point=sd.get_point(x=200, y=400), angle=80, color=sd.COLOR_YELLOW, length=150)
square(start_point=sd.get_point(x=450, y=375), angle=60, color=sd.COLOR_YELLOW, length=125)
pentagon(start_point=sd.get_point(x=200, y=100), angle=60, color=sd.COLOR_YELLOW, length=100)
hexagon(start_point=sd.get_point(x=450, y=100), angle=40, color=sd.COLOR_YELLOW, length=90)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
