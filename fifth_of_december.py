__author__ = 'martinsolheim'
import itertools

base = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def find_all_permutations(number_list):
    return set(itertools.permutations(number_list))


def combine_list_elements(number_list):
    temp = ''.join(map(str, number_list))
    return int(temp)

# Brute force that shit !!
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

permutations = find_all_permutations(base)
big_numbers = []
for number in permutations:
    big_numbers.append(combine_list_elements(number))

prime_factors = []
for number in big_numbers:
    prime_factors.append(largest_prime_factor(number))

print(min(prime_factors))
