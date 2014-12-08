__author__ = 'martinsolheim', 'mariaauneremoy'


def real_divisors(number):
    number_real_divisors = []
    for i in range(1, number):
        if number % i == 0:
            number_real_divisors.append(i)

    return number_real_divisors


def sum_real_divisors(number, number_real_divisors):
    return sum(number_real_divisors) == number


def find_answer():
    answer_list = []
    for i in range(1, 10001):
        if sum_real_divisors(i, real_divisors(i)):
            answer_list.append(i)

    return answer_list


print(find_answer())