__author__ = 'martinsolheim'

all_products = []

for i in range(1, 8001):
    for j in range(i, 8001):
        all_products.append(i * j)
    print(8000 - i, 'runs left')

print(len(set(all_products)))