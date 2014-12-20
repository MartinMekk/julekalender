__author__ = 'maria'

import math

def get_digit_sum(x, y):
    list = map(int, str(abs(x))) + map(int, str(abs(y)))
    digit_sum = 0
    for num in list:
        digit_sum += num
    return digit_sum

tiles_list = [(0,0)]
count = 1

for tile in tiles_list:
    x = tile[0]
    y = tile[1]
    if get_digit_sum(x+1, y) <= 19:
        if (x+1, y) not in tiles_list:
            tiles_list.append((x+1, y))
            if(y == 0 or x+1 == 0):
                count += 2
            else:
                count += 4
    if get_digit_sum(x, y+1) <= 19:
        if (x, y+1) not in tiles_list:
            tiles_list.append((x, y+1))
            if(y+1 == 0 or x == 0):
                count += 2
            else:
                count += 4

print count
