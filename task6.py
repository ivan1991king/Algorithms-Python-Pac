__author__ = 'Куркин Иван'

import random

num = random.randint(0, 100)
n = 10
print(f'Отгадайте число от 0 до 100')
while n > 0:
    print(f'У вас осталось {n} попыток')
    user_num = int(input('Введите число: '))
    if user_num > num:
        print("Ваше число больше")
    elif user_num < num:
        print("Ваше число меньше")
    else:
        print("Вы угадали!")
        break
    n -=1
else:
    print(f'Вы не угадали! Это число {num}')
