__author__ = 'Куркин Иван'

import string

a = int(input('Введите номер буквы латинского алфавита: '))
alphabet = string.ascii_letters

print('Это буква -', alphabet[a-1])
