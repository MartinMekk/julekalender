__author__ = 'martinsolheim'
import time
start_time = time.time()


def sum_and_power(x, y):
    return (int(''.join(list(map(str, x)))) + int(''.join(list(map(str, y))))) ** 2


def test_all_parts(num):
    num_list = list(map(int, str(num)))
    for i in range(1, len(num_list)):
        if sum_and_power(num_list[:i], num_list[i:len(num_list)]) == num:
            return True
    return False

counter = 0
for i in range(10, 1000000):
    if test_all_parts(i):
        counter += 1

print("--- %s seconds ---" % (time.time() - start_time))
print(counter)