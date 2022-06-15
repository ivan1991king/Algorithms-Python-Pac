__author__ = 'Куркин Иван'

import random

length = 20
lst = [random.randint(0, 10) for i in range(length)]

count = 0
max_count = 0
num = 0

for i in range(len(lst) - 1):
    if lst[i] != num:
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                count += 1
        if count > max_count:
            max_count = count
            num = lst[i]
        count = 0

if num == 0:
    print(lst)
    print('В массиве нет повторяющихся чисел')
else:
    print(lst)
    print(f'Число {num} встречается в массиве чаще всего, {max_count + 1} раз(а)')
