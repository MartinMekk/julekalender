__author__ = 'martinsolheim'

import os
import itertools

path_dir = os.path.dirname(__file__)
filename = os.path.join(path_dir, "data/short_primes.txt")

primes = []
with open(filename, newline='\n') as inputFile:
    for line in inputFile:
        primes.append(line.strip().split())
inputFile.close()

primes = list(itertools.chain.from_iterable(primes))
primes = list(map(int, primes))


def reverse_number(num):
    return int(str(num)[::-1])


def get_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

count = 0
for i in primes:
    if not get_palindrome(i) and is_prime(reverse_number(i)):
        count += 1

print(count)