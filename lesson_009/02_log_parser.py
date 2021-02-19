# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по дням
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

from pprint import pprint
from termcolor import cprint


class AnalysisFile:
    def __init__(self, in_filename, out_filename):
        self.in_filename = in_filename
        self.out_filename = out_filename
        self.massive_of_logs = []
        self.massive_of_log_without_OK = []
        self.grouped_logs_by_min = []
        self.grouped_logs_by_hour = []
        self.grouped_logs_by_day = []
        self.grouped_logs_by_month = []
        self.grouped_logs_by_year = []
        self.totalNOK = 0
        self.group_by = ''

    def get_log(self):
        massive_of_logs = []
        with open(file=self.in_filename, mode='r', encoding='utf-8') as file:
            for line in file:
                log = {'year': line[1:5],
                       'month': line[6:8],
                       'day': line[9:11],
                       'hour': line[12:14],
                       'min': line[15:17],
                       'sec': line[18:20],
                       'status': line[29:-1]}
                massive_of_logs.append(log)
        return massive_of_logs

    def parse_log(self, group='year'):
        """

        :param group: group 'min', 'hour', 'day', 'month', 'year':
        :return:
        """
        self.group_by = group
        for log in self.get_log():
            if log['status'] == 'NOK':
                self.massive_of_log_without_OK.append(log)
                self.totalNOK += 1
        if group == 'min' or group == 'hour' or group == 'day' or group == 'month' or group == 'year':
            i = 1
            count = 1
            length = len(self.massive_of_log_without_OK)
            # ------------------ Group by  min--------------------
            while i < length:
                if self.massive_of_log_without_OK[i]['min'] == self.massive_of_log_without_OK[i - 1]['min'] and \
                        self.massive_of_log_without_OK[i]['hour'] == self.massive_of_log_without_OK[i - 1]['hour'] and \
                        self.massive_of_log_without_OK[i]['day'] == self.massive_of_log_without_OK[i - 1]['day'] and \
                        self.massive_of_log_without_OK[i]['month'] == self.massive_of_log_without_OK[i - 1]['month'] and \
                        self.massive_of_log_without_OK[i]['year'] == self.massive_of_log_without_OK[i - 1]['year']:
                    count += 1

                    if i == (length - 1):
                        short_log = {
                            'year': self.massive_of_log_without_OK[i]['year'],
                            'month': self.massive_of_log_without_OK[i]['month'],
                            'day': self.massive_of_log_without_OK[i]['day'],
                            'hour': self.massive_of_log_without_OK[i]['hour'],
                            'min': self.massive_of_log_without_OK[i]['min'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_min.append(short_log)

                else:
                    if i == (length - 1):
                        short_log = {
                            'year': self.massive_of_log_without_OK[i - 1]['year'],
                            'month': self.massive_of_log_without_OK[i - 1]['month'],
                            'day': self.massive_of_log_without_OK[i - 1]['day'],
                            'hour': self.massive_of_log_without_OK[i - 1]['hour'],
                            'min': self.massive_of_log_without_OK[i - 1]['min'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_min.append(short_log)
                        count = 1
                        short_log = {
                            'year': self.massive_of_log_without_OK[i]['year'],
                            'month': self.massive_of_log_without_OK[i]['month'],
                            'day': self.massive_of_log_without_OK[i]['day'],
                            'hour': self.massive_of_log_without_OK[i]['hour'],
                            'min': self.massive_of_log_without_OK[i]['min'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_min.append(short_log)
                    else:
                        short_log = {
                            'year': self.massive_of_log_without_OK[i - 1]['year'],
                            'month': self.massive_of_log_without_OK[i - 1]['month'],
                            'day': self.massive_of_log_without_OK[i - 1]['day'],
                            'hour': self.massive_of_log_without_OK[i - 1]['hour'],
                            'min': self.massive_of_log_without_OK[i - 1]['min'],
                            'count': str(count)
                        }
                        count = 1
                        self.grouped_logs_by_min.append(short_log)
                i += 1
            i = 1
            count = int(self.grouped_logs_by_min[i - 1]['count'])
            length = len(self.grouped_logs_by_min)
            # ------------------ Group by hour --------------------
            while i < length:
                if self.grouped_logs_by_min[i]['hour'] == self.grouped_logs_by_min[i - 1]['hour'] and \
                        self.grouped_logs_by_min[i]['day'] == self.grouped_logs_by_min[i - 1]['day'] and \
                        self.grouped_logs_by_min[i]['month'] == self.grouped_logs_by_min[i - 1]['month'] and \
                        self.grouped_logs_by_min[i]['year'] == self.grouped_logs_by_min[i - 1]['year']:
                    count += int(self.grouped_logs_by_min[i]['count'])
                    if i == length - 1:
                        short_log = {
                            'year': self.grouped_logs_by_min[i - 1]['year'],
                            'month': self.grouped_logs_by_min[i - 1]['month'],
                            'day': self.grouped_logs_by_min[i - 1]['day'],
                            'hour': self.grouped_logs_by_min[i - 1]['hour'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_hour.append(short_log)
                else:
                    if i == length - 1:
                        short_log = {
                            'year': self.grouped_logs_by_min[i - 1]['year'],
                            'month': self.grouped_logs_by_min[i - 1]['month'],
                            'day': self.grouped_logs_by_min[i - 1]['day'],
                            'hour': self.grouped_logs_by_min[i - 1]['hour'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_hour.append(short_log)
                        count = int(self.grouped_logs_by_min[i]['count'])
                        short_log = {
                            'year': self.grouped_logs_by_min[i]['year'],
                            'month': self.grouped_logs_by_min[i]['month'],
                            'day': self.grouped_logs_by_min[i]['day'],
                            'hour': self.grouped_logs_by_min[i]['hour'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_hour.append(short_log)
                    else:
                        short_log = {
                            'year': self.grouped_logs_by_min[i - 1]['year'],
                            'month': self.grouped_logs_by_min[i - 1]['month'],
                            'day': self.grouped_logs_by_min[i - 1]['day'],
                            'hour': self.grouped_logs_by_min[i - 1]['hour'],
                            'count': str(count)
                        }
                        count = int(self.grouped_logs_by_min[i]['count'])
                        self.grouped_logs_by_hour.append(short_log)
                i += 1
            i = 1
            count = int(self.grouped_logs_by_hour[i - 1]['count'])
            length = len(self.grouped_logs_by_hour)
            # ------------------ Group by  day--------------------
            while i < length:
                if self.grouped_logs_by_hour[i]['day'] == self.grouped_logs_by_hour[i - 1]['day'] and \
                        self.grouped_logs_by_hour[i]['month'] == self.grouped_logs_by_hour[i - 1]['month'] and \
                        self.grouped_logs_by_hour[i]['year'] == self.grouped_logs_by_hour[i - 1]['year']:
                    count += int(self.grouped_logs_by_hour[i]['count'])
                    if i == length - 1:
                        short_log = {
                            'year': self.grouped_logs_by_hour[i - 1]['year'],
                            'month': self.grouped_logs_by_hour[i - 1]['month'],
                            'day': self.grouped_logs_by_hour[i - 1]['day'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_day.append(short_log)
                else:
                    if i == length - 1:
                        short_log = {
                            'year': self.grouped_logs_by_hour[i - 1]['year'],
                            'month': self.grouped_logs_by_hour[i - 1]['month'],
                            'day': self.grouped_logs_by_hour[i - 1]['day'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_day.append(short_log)
                        count = int(self.grouped_logs_by_hour[i]['count'])
                        short_log = {
                            'year': self.grouped_logs_by_hour[i]['year'],
                            'month': self.grouped_logs_by_hour[i]['month'],
                            'day': self.grouped_logs_by_hour[i]['day'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_day.append(short_log)
                    else:
                        short_log = {
                            'year': self.grouped_logs_by_hour[i - 1]['year'],
                            'month': self.grouped_logs_by_hour[i - 1]['month'],
                            'day': self.grouped_logs_by_hour[i - 1]['day'],
                            'count': str(count)
                        }
                        count = int(self.grouped_logs_by_hour[i]['count'])
                        self.grouped_logs_by_day.append(short_log)
                i += 1
            i = 1
            count = int(self.grouped_logs_by_day[i - 1]['count'])
            length = len(self.grouped_logs_by_day)
            # ------------------ Group by month --------------------
            while i < length:
                if self.grouped_logs_by_day[i]['month'] == self.grouped_logs_by_day[i - 1]['month'] and \
                        self.grouped_logs_by_day[i]['year'] == self.grouped_logs_by_day[i - 1]['year']:
                    count += int(self.grouped_logs_by_day[i]['count'])
                    if i == length - 1:
                        short_log = {
                            'year': self.grouped_logs_by_day[i - 1]['year'],
                            'month': self.grouped_logs_by_day[i - 1]['month'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_month.append(short_log)
                else:
                    if i == length - 1:
                        short_log = {
                            'year': self.grouped_logs_by_day[i - 1]['year'],
                            'month': self.grouped_logs_by_day[i - 1]['month'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_month.append(short_log)
                        count = int(self.grouped_logs_by_day[i]['count'])
                        short_log = {
                            'year': self.grouped_logs_by_day[i]['year'],
                            'month': self.grouped_logs_by_day[i]['month'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_month.append(short_log)
                    else:
                        short_log = {
                            'year': self.grouped_logs_by_day[i - 1]['year'],
                            'month': self.grouped_logs_by_day[i - 1]['month'],
                            'count': str(count)
                        }
                        count = int(self.grouped_logs_by_day[i]['count'])
                        self.grouped_logs_by_month.append(short_log)
                i += 1
            i = 1
            count = int(self.grouped_logs_by_month[i - 1]['count'])
            length = len(self.grouped_logs_by_month)
            # ------------------ Group by year --------------------
            while i < length:
                if self.grouped_logs_by_month[i]['year'] == self.grouped_logs_by_month[i - 1]['year']:
                    count += int(self.grouped_logs_by_month[i]['count'])
                    if i == length - 1:
                        short_log = {
                            'year': self.grouped_logs_by_month[i - 1]['year'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_year.append(short_log)
                else:
                    if i == length - 1:
                        short_log = {
                            'year': self.grouped_logs_by_month[i - 1]['year'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_year.append(short_log)
                        count = int(self.grouped_logs_by_month[i]['count'])
                        short_log = {
                            'year': self.grouped_logs_by_month[i]['year'],
                            'count': str(count)
                        }
                        self.grouped_logs_by_year.append(short_log)
                    else:
                        short_log = {
                            'year': self.grouped_logs_by_month[i - 1]['year'],
                            'count': str(count)
                        }
                        count = int(self.grouped_logs_by_month[i]['count'])
                        self.grouped_logs_by_year.append(short_log)
                i += 1
            if group == 'min':
                return self.grouped_logs_by_min
            elif group == 'day':
                return self.grouped_logs_by_day
            elif group == 'hour':
                return self.grouped_logs_by_hour
            elif group == 'month':
                return self.grouped_logs_by_month
            elif group == 'year':
                return self.grouped_logs_by_year
        else:
            return False


    def test(self):
        total_1 = 0
        for _dict in self.grouped_logs_by_min:
            total_1 += int(_dict['count'])
        total_2 = 0
        for _dict in self.grouped_logs_by_hour:
            total_2 += int(_dict['count'])
        total_3 = 0
        for _dict in self.grouped_logs_by_day:
            total_3 += int(_dict['count'])
        total_4 = 0
        for _dict in self.grouped_logs_by_month:
            total_4 += int(_dict['count'])
        total_5 = 0
        for _dict in self.grouped_logs_by_month:
            total_5 += int(_dict['count'])
        cprint('NOK Groped by hour', color='yellow')
        pprint(self.grouped_logs_by_hour)
        cprint('NOK Groped by day', color='yellow')
        pprint(self.grouped_logs_by_day)
        cprint('NOK Groped by month', color='yellow')
        pprint(self.grouped_logs_by_month)
        cprint('NOK Groped by year', color='yellow')
        pprint(self.grouped_logs_by_year)
        cprint('-'*40, color='yellow')
        pprint(f'TotalNOK : {self.totalNOK}')
        pprint(f'Total_by_min : {total_1}')
        pprint(f'Total_by_hour : {total_2}')
        pprint(f'Total_by_day : {total_3}')
        pprint(f'Total_by_month : {total_4}')
        pprint(f'Total_by_year : {total_5}')
        if self.totalNOK == total_1 == total_2 == total_3 == total_4 == total_5:
            cprint('Test: OK', color='green')
        else:
            cprint('Test: False', color='red')

    def write_log(self):
        filename = self.out_filename
        if filename is not None:
            file = open(filename, 'w', encoding='utf-8')
        else:
            file = None
        if self.group_by == "year":
            file.write("Группировка по годам\n")
            file.write("--------------------\n")
            for _dict in self.grouped_logs_by_year:
                string = f'[{_dict["year"]}] {_dict["count"]}\n'
                file.write(string)
        if self.group_by == "month":
            file.write("Группировка по месяцам\n")
            file.write("----------------------\n")
            for _dict in self.grouped_logs_by_month:
                string = f'[{_dict["year"]}-{_dict["month"]}] {_dict["count"]}\n'
                file.write(string)
        if self.group_by == "day":
            file.write("Группировка по дням\n")
            file.write("-------------------\n")
            for _dict in self.grouped_logs_by_day:
                string = f'[{_dict["year"]}-{_dict["month"]}-{_dict["day"]}] {_dict["count"]}\n'
                file.write(string)
        if self.group_by == "hour":
            file.write("Группировка по часам\n")
            file.write("--------------------\n")
            for _dict in self.grouped_logs_by_hour:
                string = f'[{_dict["year"]}-{_dict["month"]}-{_dict["day"]} {_dict["hour"]}h] {_dict["count"]}\n'
                file.write(string)
        if self.group_by == "min":
            file.write("Группировка по минутам\n")
            file.write("----------------------\n")
            for _dict in self.grouped_logs_by_min:
                string = f'[{_dict["year"]}-{_dict["month"]}-{_dict["day"]} {_dict["hour"]}:' \
                         f'{_dict["min"]}] {_dict["count"]}\n'
                file.write(string)
        if file:
            file.close()


analyser = AnalysisFile("events.txt", "log\out_logs.txt")
analyser.parse_log(group='hour')
analyser.test()
analyser.write_log()
