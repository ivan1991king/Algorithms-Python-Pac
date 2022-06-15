__author__ = 'Куркин Иван'

import random

length = 10
lst = [random.randint(0, 100) for i in range(length)]
print(lst)

min1_d = lst[0]
min2_d = lst[1]
min1_i = 0

for i in range(1, len(lst)):
    if lst[i] < min1_d:
        min1_d = lst[i]
        min1_i = i
lst.pop(min1_i)
for i in range(1, len(lst)):
    if lst[i] < min2_d:
        min2_d = lst[i]
print(min1_d, min2_d)
