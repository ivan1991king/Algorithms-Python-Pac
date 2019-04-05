__author__ = 'Куркин Иван'

#за базу взял первую задачу из дз к 3 уроку, т.к. алгоритм выполняется за явно большое кол-во времени
#В диапазоне натуральных чисел от 2 до 1000000 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
#Попробовал для знвачений диапазона 10000 и 1000000

import timeit
import cProfile

def spisok(n):
    spisok={}
    for x in range(2, n*n+1):
        for y in range(1, 10):
            if x % y == 0:
                if y in spisok:
                    spisok[y] += 1
                else:
                    spisok[y] = 1
    print(spisok)

#решение задачи другим способом для сравнения
def spisok2(n):
    lst1 = [i for i in range(2, n*n)]
    lst2 = [i for i in range(2, 10)]
    summ = [0] * len(lst2)
    for i in range(len(lst2)):
        for j in range(len(lst1)):
            if lst1[j] % lst2[i] == 0:
                summ[i] += 1
        print(f'{lst2[i]}: {summ[i]}')

statement = "spisok(100)"
setup = "from __main__ import spisok"
print(timeit.timeit(statement, setup=setup, number=1))
statement = "spisok2(100)"
setup = "from __main__ import spisok2"
print(timeit.timeit(statement, setup=setup, number=1))
#Результат решения 1: 0.030105405000000002
#Результат решения 2: 0.030580615000000005

statement = "spisok(1000)"
setup = "from __main__ import spisok"
print(timeit.timeit(statement, setup=setup, number=1))
statement = "spisok2(1000)"
setup = "from __main__ import spisok2"
print(timeit.timeit(statement, setup=setup, number=1))
#Результат решения 1: 4.341108054
#Результат решения 2: 3.551977207

cProfile.run('spisok(1000)')
#Результат решения 1: 3.468

cProfile.run('spisok2(1000)')
#Результат решения 2: 3.424

#Вывод: второе решение задачи выполняется быстрее
