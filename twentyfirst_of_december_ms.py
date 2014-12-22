__author__ = 'martinsolheim'

import os

path_dir = os.path.dirname(__file__)
filename = os.path.join(path_dir, "data/word_list.txt")

word_list = []
with open(filename, newline='\n') as inputFile:
    for line in inputFile:
        word_list.append(line.strip())
inputFile.close()
sum_list = []

for i in word_list:
    sum_list.append(sum(map(ord, i)))

sorted_sum_list = sorted(sum_list)
sorted_sum_list = sorted_sum_list[::-1]
answer_sum = 0
for i in range(0, 42):
    answer_sum += sorted_sum_list[i]

print(answer_sum)