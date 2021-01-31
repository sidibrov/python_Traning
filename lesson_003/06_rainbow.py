# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

sd.resolution = (1000, 800)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# y_start, y_end = 50, 450
# for i in rainbow_colors:
#     start_point = sd.get_point(50, y_start)
#     end_point = sd.get_point(350, y_end)
#     sd.line(start_point, end_point, i, width=15)
#     y_start += 20
#     y_end += 20

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с пSараметрами, что бы было красиво
radius = 700
point = sd.get_point(500, -200)
for i in rainbow_colors:
    sd.circle(center_position=point, radius=radius, color=i, width=20)
    radius += 20
sd.pause()
