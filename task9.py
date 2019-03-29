__author__ = 'Куркин Иван'

import random
import pprint

def generate_matr(rows, cols):
    matr = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(1, 100))
        matr.append(row)
    return matr

def find_max(matr):
    matr = list(zip(*matr))     #легче искать минимумы по строчкам
    lst_max = []
    for i in range(len(matr)):
        m = matr[i][0]
        for j in range(1, len(matr[i])):
            if matr[i][j] < m:
                m = matr[i][j]
        lst_max.append(m)
    return max(lst_max)

matr55 = generate_matr(5,5)
pprint.pprint(matr55, width=40)
print(find_max(matr55))
