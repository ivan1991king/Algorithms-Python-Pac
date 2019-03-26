__author__ = 'Куркин Иван'

count = 1
for x in range(32, 128):
    print(f"{x}-{chr(x)}", end=" ")
    if count % 10 == 0:
        print()
    count += 1
