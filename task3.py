__author__ = 'Куркин Иван'

import random

length = 10
lst = [random.randint(0, 100) for i in range(length)]
print(lst)

min_d = lst[0]
max_d = lst[0]
min_i = 0
max_i = 0

for i in range(1, len(lst)):
    if lst[i] > max_d:
        max_d = lst[i]
        max_i = i
    if lst[i] < min_d:
        min_d = lst[i]
        min_i = i

lst[max_i], lst[min_i] = lst[min_i], lst[max_i]
print(lst)
