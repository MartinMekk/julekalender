__author__ = 'maria'

def is_number_correct(number):
    first_number = ""
    number_list = map(str, str(number))
    for i in range(0, len(number_list)-1):
        first_number += number_list[i]
        second_number = ''.join(number_list[i+1:len(number_list)])
        if (int(first_number) + int(second_number))**2 == number:
            return True
    return False

count = 0
for n in range(10, 1000000):
    if is_number_correct(n):
        count += 1

print count
