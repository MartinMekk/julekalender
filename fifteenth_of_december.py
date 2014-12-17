__author__ = 'martinsolheim'


def dividable_by_ten(num):
    return num % 10 == 0


def dividable_by_ten_rule(x, y):
    return not (dividable_by_ten(x) and dividable_by_ten(y))


def has_four_digits(num):
    return 999 < num < 10000


def contains_same_digits(x, y, n):
    ls_xy = list(map(int, str(x))) + (list(map(int, str(y))))
    ls_n = list(map(int, str(n)))

    return sorted(ls_xy) == sorted(ls_n)


all_n = []
for i in range(10, 100):
    for j in range(i, 100):
        temp = i * j
        if contains_same_digits(i, j, temp) and has_four_digits(temp):
            all_n.append(temp)

print(len(set(all_n)))
print(sum([sorted(str(x) + str(y)) == sorted(str(x*y)) for x in range(10,100) for y in range(10,100)])/2)