__author__ = 'martinsolheim'

contain = "472047"
for n in range(1, 10001):
    if contain in str(2**n):
        print(n)
        break