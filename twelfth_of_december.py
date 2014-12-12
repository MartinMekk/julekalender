__author__ = 'martinsolheim'

import datetime as dt

num_friday_thirteenth = 0

for i in range(1337, 2015):
    for j in range(1, 13):
        if dt.date(i, j, 13).weekday() == 4:
            num_friday_thirteenth += 1

print(num_friday_thirteenth)