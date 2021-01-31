# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
brick = (100, 50)  # Size of the brick
sd.resolution = (1200, 600)  # Size of the wall
sd.background_color = sd.COLOR_RED  # Color of the wall
count = 0  # для кирпичной кладки в 1/2 кирпича (ложковая)
for y in range(0, sd.resolution[1] + 1, brick[1]):
    count += 1
    for x in range(0, sd.resolution[0] + 1, brick[0]):
        sd.line(start_point=sd.get_point(x, y), end_point=sd.get_point(x + 100, y), color=sd.COLOR_BLACK, width=2)

        if count % 2 == 0:
            sd.line(start_point=sd.get_point(x, y), end_point=sd.get_point(x, y + brick[1]), color=sd.COLOR_BLACK,
                    width=2)
        else:
            sd.line(start_point=sd.get_point(x - brick[0] / 2, y),
                    end_point=sd.get_point(x - brick[0] / 2, y + brick[1]), color=sd.COLOR_BLACK, width=2)

sd.pause()
