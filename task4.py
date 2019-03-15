__author__ = 'Куркин Иван'

import random

print('Введите диапазон целых чисел:')
int1 = int(input('число 1 = '))
int2 = int(input('число 2 = '))

print('Введите диапазон вещественных чисел:')
float1 = float(input('число 1 = '))
float2 = float(input('число 2 = '))

print('Введите диапазон символов:')
symb1 = ord(input('символ 1 = '))
symb2 = ord(input('символ 2 = '))

rand_int = random.randint(int1, int2)
rand_float = random.uniform(float1, float2)
rand_symb = chr(random.randint(symb1,symb2))

print(f'Случайное целое число в диапазоне от {int1} до {int2}: {rand_int}')
print(f'Случайное вещественное число в диапазоне от {float1} до {float2}: {rand_float}')
print(f'Случайный символ в диапазоне от {chr(symb1)} до {chr(symb2)}: {rand_symb}')
