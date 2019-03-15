__author__ = 'Куркин Иван'

print('Введите три разных числа')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if  b < a < c or c < a < b:
    print('Среднее число: a')
elif a < b < c or c < b < a:
    print('Среднее число: b')
else:
    print('Среднее число: c')
