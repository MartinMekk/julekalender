__author__ = 'martinsolheim'

import os
import itertools


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def find_n(read_list, search_range):
    write_list = []
    for j in range(len(primes)):
        temp = 0
        for i in range(0, search_range):
            if (i + j) >= len(primes)-1:
                print("rettt")
                return write_list
            temp += primes[i + j]
        if temp in read_list:
            write_list.append(temp)
        elif temp > read_list[len(read_list)-1]:
            return write_list

path_dir = os.path.dirname(__file__)
filename = os.path.join(path_dir, "data/primes.txt")

primes = []
with open(filename, newline='\n') as inputFile:
    for line in inputFile:
        primes.append(line.strip().split())
inputFile.close()

primes = list(itertools.chain.from_iterable(primes))
primes = list(map(int, primes))

results_541 = []

for j in range(len(primes)):
    temp = 0
    for i in range(0, 541):
        temp += primes[i + j]
    if temp < 10000000 and is_prime(temp):
        results_541.append(temp)
    elif temp > 10000000:
        break

print(results_541)
results_41 = find_n(results_541, 41)
print(results_41)
results_17 = find_n(results_41, 17)
print(results_17)
#results_7 = find_n(results_17, 7)
#print(results_7)
