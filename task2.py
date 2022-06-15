__author__ = 'Куркин Иван'

import random

length = 10

lst1 = [random.randint(0, 100) for i in range(length)]
lst2 = []

for i in range(len(lst1)):
    if lst1[i] % 2 == 0:
        lst2.append(i)

print("Дан список:", lst1)
print("Список индексов четных чисел данного списка", lst2)
