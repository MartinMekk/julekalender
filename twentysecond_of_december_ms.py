__author__ = 'martinsolheim'
import numpy as np
from collections import defaultdict
import time
start_time = time.time()

def can_reduce_with_square(num):
    visited = defaultdict(int)
    while num != 1:
        visited[num] += 1
        if visited[num] > 1:
            return False
        num = sum(np.power(list(map(int, str(num))), 2))
    return True

num_list = []
for i in range(1, 50):
    if can_reduce_with_square(i):
        num_list.append(i)

print("--- %s seconds ---" % (time.time() - start_time))
print(num_list)