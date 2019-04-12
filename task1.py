__author__ = 'Куркин Иван'


import random
import sys

# Функция для подсчета объема занятой памяти

def calc_size(x):
    sum_key = 0
    sum_value = 0
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                sum_key = sum_key + sys.getsizeof(key)
                print(f'type = {type(key)}, size = {sys.getsizeof(key)}, object = {key}')
                sum_value = sum_value + sys.getsizeof(value)
                print(f'type = {type(value)}, size = {sys.getsizeof(value)}, object = {value}')
            print(f'Память, занятая ссылками на переменные = {sum_key}')
            print(f'Память, занятая значениями переменных = {sum_value}')
    print(f'Память, занятая функцией = {sys.getsizeof(x)}')
    print(f'Всего занято памяти: {sys.getsizeof(x) + sum_key + sum_value}')


# 3 задача 3 урока

def change_places():
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
    return vars()


# 4 задача 3 урока

def find_count():
    length=20
    lst=[random.randint(0, 10) for i in range(length)]

    count=0
    max_count=0
    num=0

    for i in range(len(lst) - 1):
        if lst[i] != num:
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j]:
                    count+=1
            if count > max_count:
                max_count=count
                num=lst[i]
            count=0

    if num == 0:
        print(lst)
        print('В массиве нет повторяющихся чисел')
    else:
        print(lst)
        print(f'Число {num} встречается в массиве чаще всего, {max_count + 1} раз(а)')
    return vars()
calc_size(change_places())
print()
calc_size(find_count())


#Windows 7, 64-разрядная ОС, Python 3.7
#Чем больше переменных, тем больше памяти занимает
#Ссылки занимают больше памяти, чем сами значения, если это не списки.
#Списки очень тяжелые
