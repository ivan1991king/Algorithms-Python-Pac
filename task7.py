__author__ = 'Куркин Иван'

n = int(input("Введите число n: "))

print("1+2+...+n:", sum(range(1, n + 1)))
print("n(n+1)/2:", n * (n + 1) / 2)
if sum(range(1, n + 1)) == n * (n + 1) / 2:
    print("Равенство выполняется")
else:
    print("Равенство не выполняется")
