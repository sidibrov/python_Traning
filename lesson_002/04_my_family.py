#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['отец', 'мать', 'сын']
my_family.append('дедушка')

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['отец', 180],
    ['мать', 170],
    ['сын', 110],
    ['дедушка', 160],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца - ' + str(my_family_height[0][1]) + ' см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum_height = int(my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1])
print('Общий рост моей семьи - '  + str(sum_height) + ' см')