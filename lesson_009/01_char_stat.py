# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
import zipfile
from pprint import pprint


class TextStatistic:
    def __init__(self, filename):
        self.file_name = filename
        # self.stat_massive = []
        self.stat = {}
        self.total = 0

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def get_stat(self):
        if self.file_name.endswith(".zip"):
            self.unzip()
        with open(file=self.file_name, mode="r", encoding="cp1251") as file:
            for line in file:
                for i in line:
                    if i.isalpha():
                        self.total += 1
                        if i in self.stat:
                            self.stat[i] += 1
                        else:
                            self.stat[i] = 1
        pass

    def stat_sort(self, order="decrease_by_count"):
        """
        :param order: "decrease_by_count", "increase_by_count", "decrease_by_char", "increase_by_char",
        :return: sorted by order massive of tuples  [(char, count),...]
        """
        if order == 'decrease_by_count':
            stat_sorted = sorted(self.stat.items(), key=lambda x: x[1], reverse=True)
        elif order == 'increase_by_count':
            stat_sorted = sorted(self.stat.items(), key=lambda x: x[1], reverse=False)
        elif order == 'decrease_by_char':
            stat_sorted = sorted(self.stat.items(), key=lambda x: x[0], reverse=True)
        elif order == 'increase_by_char':
            stat_sorted = sorted(self.stat.items(), key=lambda x: x[0], reverse=False)
        else:
            return False
        return stat_sorted
        #  if order == 'decrease_by_count':
        #     for char, count in self.stat.items():
        #         stat_sorted.append([count, char])
        #     stat_sorted.sort(reverse=True)
        # elif order == 'increase_by_count':
        #     for char, count in self.stat.items():
        #         stat_sorted.append([count, char])
        #     stat_sorted.sort(reverse=False)
        # elif order == 'decrease_by_char':
        #     for char, count in self.stat.items():
        #         stat_sorted.append([char, count])
        #     stat_sorted.sort(reverse=True)
        # elif order == 'increase_by_char':
        #     for char, count in self.stat.items():
        #         stat_sorted.append([char, count])
        #     stat_sorted.sort(reverse=False)
        # else:
        #     return False
        # return stat_sorted

    def print_one_string_of_table(self, char, count):
        if count >= 100000:
            print(f"|    {char}    |  {count}  |")
        elif count >= 10000:
            print(f"|    {char}    |   {count}  |")
        elif count >= 1000:
            print(f"|    {char}    |    {count}  |")
        elif count >= 100:
            print(f"|    {char}    |     {count}  |")
        elif count >= 10:
            print(f"|    {char}    |      {count}  |")
        else:
            print(f"|    {char}    |       {count}  |")

    def print_stat(self, order='decrease_by_count'):
        if order == 'decrease_by_count' or \
                order == 'increase_by_count' or \
                order == 'decrease_by_char' or \
                order == 'increase_by_char':
            print(f"+---------+----------+\n|  {order} |")
            print(f"+---------+----------+\n|  буква  | частота  |\n+---------+----------+")
            for char, count in self.stat_sort(order=order):
                self.print_one_string_of_table(char, count)
        else:
            return False


text_statistic = TextStatistic(filename="voyna-i-mir.txt.zip")
text_statistic.get_stat()
text_statistic.print_stat(order='decrease_by_count')
text_statistic.print_stat(order='increase_by_count')
text_statistic.print_stat(order='decrease_by_char')
text_statistic.print_stat(order='increase_by_char')
print(f"+---------+----------+\n|  ИТОГО  | {text_statistic.total}  |\n+---------+----------+")
