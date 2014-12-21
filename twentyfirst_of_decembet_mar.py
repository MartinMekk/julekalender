__author__ = 'maria'

import os


def find_ascii_value(word):
    character_list = list(word)
    ascii_value = 0
    for character in character_list:
        ascii_value += ord(character)
    return ascii_value

path_dir = os.path.dirname(__file__)
filename = os.path.join(path_dir, "data/word_list.txt")

words = []
with open(filename, "r") as inputFile:
    for line in inputFile:
        words.append(line.strip())
inputFile.close()

word_dict = {}
for word in words:
    word_dict[word] = find_ascii_value(word)

keys_of_largest_ascii_values = sorted(word_dict, key=word_dict.get, reverse=True)[:42]

sum = 0
for key in keys_of_largest_ascii_values:
    sum += word_dict[key]

print sum

