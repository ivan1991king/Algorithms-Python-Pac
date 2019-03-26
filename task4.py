__author__ = 'Куркин Иван'

n = int(input('Введите кол-во элементов ряда: '))
a = 1
b = []
sum_b = 0

for x in range(n):
    b.append(a)
    sum_b += a
    a /= -2
print(b)
print(sum_b)
