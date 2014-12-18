__author__ = 'martinsolheim'

import os
from collections import defaultdict

path_dir = os.path.dirname(__file__)
filename = os.path.join(path_dir, "data/word_list.txt")

words = []
with open(filename, newline='\n') as inputFile:
    for line in inputFile:
        words.append(line.strip())
inputFile.close()

word_dict = defaultdict(int)
for word in words:
    word_dict[''.join(sorted(word.lower()))] += 1

print(max(word_dict, key=word_dict.get))
print(word_dict['agnor'])