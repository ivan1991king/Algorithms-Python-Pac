__author__ = 'Куркин Иван'

print('Введите координаты двух точек:')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

if x1 == x2:
    print(f'Уравнение прямой: x = {x1}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'Уравнение прямой: y = {k}x + {b}')
