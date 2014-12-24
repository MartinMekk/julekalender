__author__ = 'martinsolheim'


def last_digit_check(num):
    return str(num)[-1] == '6'


def move_last_digit_check(num):
    list_num = list(map(int, str(num)))
    list_num.insert(0, list_num.pop(list_num.index(list_num[-1])))
    return num * 4 == int(''.join(list(map(str, list_num))))


for i in range(10, 1000000):
    if last_digit_check(i) and move_last_digit_check(i):
        print(i)
        break