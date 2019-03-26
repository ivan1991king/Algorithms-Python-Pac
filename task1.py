__author__ = 'Куркин Иван'

#учимся писать красиво

import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
    }

while True:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    znak = input("Введите знак операции -+*/ или 0 для выхода: ")

    if znak not in operations:
        print("Неверный символ, введите -+*/ или 0 для выхода")

    elif znak == '/' and b == 0:
        print("Деление на ноль запрещено")
        continue

    elif znak == '0':
        print("Конец")
        break

    print(operations[znak](a, b))
