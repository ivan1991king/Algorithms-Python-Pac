__author__ = 'Куркин Иван'

import random

length = 10
lst = [random.randint(0, 10) for i in range(length)]
print(lst)

min_d = lst[0]
max_d = lst[0]
max_i=0
min_i=0

for i in range(1, len(lst)):
    if lst[i] > max_d:
        max_d = lst[i]
        max_i = i
    if lst[i] < min_d:
        min_d = lst[i]
        min_i = i
summa = 0
print(min_i, max_i)
if min_i+1 < max_i:
    for i in range(min_i+1, max_i):
        summa += lst[i]
    print(f"Сумма чисел между мин и макс: {summa}")
elif min_i > max_i+1:
    for i in range(max_i+1, min_i):
        summa += lst[i]
    print(f"Сумма чисел между мин и макс: {summa}")
else:
    print("Нет элементв между экстремумами")
