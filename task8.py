__author__ = 'Куркин Иван'

import pprint

def generate_matr(rows, cols):
    matr = []
    for i in range(rows):
        row = []
        summa = 0
        for j in range(cols-1):
            row.append(int(input(f"Введите элемент матрицы [{i}][{j}] : ")))
            summa = summa+row[j]
        row.append(summa)
        matr.append(row)
    return matr

matr54 = generate_matr(5,4)
pprint.pprint(matr54, width=40)