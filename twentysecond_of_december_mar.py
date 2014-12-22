__author__ = 'maria'

result_list = [1]


def square_of_integers(int_list):
    sum_of_square = 0
    for i in int_list:
        sum_of_square += i**2
    return sum_of_square

for i in range(2, 51):
    square_results = []
    square = square_of_integers(map(int, str(i)))
    while square not in square_results:
        if square == 1:
            result_list.append(i)
            break
        elif square in square_results:
            break
        square_results.append(square)
        square = square_of_integers(map(int, str(square)))

print result_list