__author__ = 'martinsolheim'

import math
sum_num = 3


def number_to_list(num):
    return list(map(int, str(num)))


def control_number(num):
    num_list = number_to_list(num)
    len_num = len(num_list)

    if len_num % 2:
        middle_index = int(len_num / 2)
        middle_value = num_list[middle_index]
        if middle_value == 1 or middle_value == 0 or middle_value == 8:
            num_list.pop(middle_index)
        else:
            return False

    for i in range(int(len_num / 2)):
        first_num = num_list[i]
        last_num = num_list[-1 - i]
        valid_num = first_num == 0 or first_num == 1 or first_num == 8
        if (valid_num and first_num == last_num) or (first_num == 9 and last_num == 6) or (first_num == 6 and last_num == 9):
            continue
        else:
            return False

    return True

for i in range(10, 100000):
    if control_number(i):
        sum_num += 1
    print(100000 - i)

print(sum_num)