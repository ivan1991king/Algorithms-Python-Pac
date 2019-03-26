__author__ = 'Куркин Иван'

a = input("Введите число: ")
dig = input("Введите цифру: ")
count = 0
count = sum([count+1 for x in a if int(dig) == int(x)])
print(count)
