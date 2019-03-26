__author__ = 'Куркин Иван'

a = input('Введите натуральное число: ')
even_d = []
uneven_d = []
count_e = 0
count_u = 0
for x in a:
    if int(x) % 2 == 0:
        even_d.append(int(x))
        count_e += 1
    else:
        uneven_d.append(int(x))
        count_u +=1
print(f'В данном числе {count_e} четные цифры: {even_d} \nи {count_u} нечетные цифры: {uneven_d}')
