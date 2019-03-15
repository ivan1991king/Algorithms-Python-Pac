__author__ = 'Куркин Иван'

print('Введите длины трех отрехков')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Треугольник не существует')
elif a != b and a != c and b != c:
    print('Тругольник разносторонний')
elif a == b == c:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')
