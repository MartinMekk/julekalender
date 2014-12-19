__author__ = 'martinsolheim'
import os
from collections import defaultdict

path_dir = os.path.dirname(__file__)
filename = os.path.join(path_dir, "data/long_string.txt")


with open(filename, newline='\n') as inputFile:
    for line in inputFile:
        long_string = line.strip()
inputFile.close()


print(long_string)
word_dict = defaultdict(int)


def is_palindrome_list(n):
    return ''.join(n) == ''.join(n)[::-1]

longest_palindrome = ""
length = len(long_string)
for i in range(length):
    first_letter = long_string[i]
    temp_test_list = [first_letter]
    for j in range(i + 1, length):
        next_letter = long_string[j]
        temp_test_list.append(next_letter)
        if first_letter == next_letter and is_palindrome_list(temp_test_list):
            if len(longest_palindrome) < len(temp_test_list):
                longest_palindrome = ''.join(temp_test_list)

print(longest_palindrome)