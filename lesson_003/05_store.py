# -*- coding: utf-8 -*-
from pprint import pprint
# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе
quantity_items = {}
total = {}
for x in goods:
    quantity_items[goods[x]] = 0
    total[goods[x]] = 0
    for y in store[goods[x]]:
        quantity_items[goods[x]] = quantity_items[goods[x]] + y['quantity']
        total[goods[x]] = total[goods[x]] + y['price']*y['quantity']
    # print(x + ' -', quantity_items[goods[x]], 'шт., стоимость', total[goods[x]], ' руб.')
    # print(f'{x} - {quantity_items[goods[x]]} шт., стоимость {total[goods[x]]} руб.')
    _str = f'{x} - {quantity_items[goods[x]]} шт., стоимость {total[goods[x]]} руб.'
    print(_str)
# pprint(total)
# pprint(quantity_items)

