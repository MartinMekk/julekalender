__author__ = 'martinsolheim'

import itertools

base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def find_all_permutations(number_list):
    return set(itertools.permutations(number_list))


def combine_list_to_number(int_list):
    return int(''.join(map(str, int_list)))

all_permutations = find_all_permutations(base)
smallest_link_number = 1000

for permutation in all_permutations:
    if permutation[0] == 0 or permutation[3] == 0 or permutation[6] == 0:
        continue
    else:
        first_number = combine_list_to_number(permutation[0:3])
        second_number = combine_list_to_number(permutation[3:6])
        if first_number + second_number == combine_list_to_number(permutation[6:10]):
            if first_number < smallest_link_number:
                smallest_link_number = first_number
            if second_number < smallest_link_number:
                smallest_link_number = second_number

print(smallest_link_number)