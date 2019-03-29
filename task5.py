__author__ = 'Куркин Иван'

import random

length = 10
lst = [random.randint(-100, 100) for i in range(length)]
print(lst)

min_d = -100
min_i = 0

for i in range(0, len(lst)):
    if min_d < lst[i] < 0:
        min_d = lst[i]
        min_i = i

print(f"Максимальный отрицательный элемент в списке: {min_d}, его индекс {min_i}")
