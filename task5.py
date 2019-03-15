__author__ = 'Куркин Иван'

import string

print('Введите 2 буквы латинского алфавита:')
a = (input('Первая буква: '))
b = (input('Вторая буква: '))

alphabet = string.ascii_letters
pos_a = alphabet.index(a)+1
pos_b = alphabet.index(b)+1
count = abs(pos_a - pos_b) - 1

print(f'Позиция первой буквы: {pos_a}, позиция второй буквы: {pos_b}, букв между ними: {count}')