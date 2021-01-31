# -*- coding: utf-8 -*-
import room_1
import room_2

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
all_district = []
for i in room_1.folks:
    all_district.append(i)
for i in room_2.folks:
    all_district.append(i)
str_all_district = ''
for i in range(0, len(all_district), 1):
    if str_all_district:
        str_all_district += ', '
    str_all_district += all_district[i]
print(f'На районе живут: {str_all_district}')
print('На районе живут:', ', '.join(all_district))
