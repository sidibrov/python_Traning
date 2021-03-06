# -*- coding: utf-8 -*-

import simple_draw as sd
from random import choice, randint

sd.resolution = (1000, 1000)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
def draw_branches(start_point, angle, length):
    if length < 3:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    if length > 6:
        v1.draw()
    else:
        v1.draw(color= sd.COLOR_GREEN)
    draw_branches(start_point=v1.end_point, angle=angle - 30 + randint(-12, 12),
                  length=length * 0.75 * randint(8, 12) / 10)
    draw_branches(start_point=v1.end_point, angle=angle + 30 + randint(-12, 12),
                  length=length * 0.75 * randint(8, 12) / 10)
    pass


root_point = sd.get_point(500, 30)
draw_branches(start_point=root_point, angle=90, length=100)
# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
sd.random_number()

sd.pause()
