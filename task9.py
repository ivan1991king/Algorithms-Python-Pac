__author__ = 'Куркин Иван'

numList = list(input('Введите числа через пробел: ').split())
sums = []
for num in numList:
    sums += [sum(map(int, list(num)))]
print("Наибольшее по сумме цифр число:", numList[sums.index(max(sums))])
print("Максимальная сумма цифр:", max(sums))
