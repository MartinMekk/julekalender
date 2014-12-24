__author__ = 'maria'


def four_times_greater(number):
    number_list = map(int, number)
    number_list.insert(0, number_list.pop(number_list.index(number_list[-1])))
    new_number = int(''.join(list(map(str, number_list))))
    return new_number == int(number) * 4


i = 2
num = str(i) + "6"

for i in range(10, 1000000):
    if four_times_greater(str(i) + "6"):
        print i
        break
