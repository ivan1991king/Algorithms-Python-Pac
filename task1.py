__author__ = 'Куркин Иван'

spisok = {}
for x in range(2, 1000000+1):
    for y in range(1, 10):
        if x % y == 0:
            if y in spisok:
                spisok[y] += 1
            else:
                spisok[y] = 1
print(spisok)
