__author__ = 'Куркин Иван'

def ulitka(n):
    #создадим нулевую матрицу
    matr = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matr.append(row)

    # заполним матрицу по спирали
    a = 1
    count = 0
    while a <= n**2:
        for j in range(count, n-count):
            matr[count][j] = a
            a += 1
        for i in range(1+count, n-count):
            matr[i][n-1-count] = a
            a += 1
        for j in range(n-1-count, count, -1):
           matr[n-1-count][j-1] = a
           a += 1
        for i in range(n-2-count, count, -1):
            matr[i][count] = a
            a += 1
        count += 1

    # преобразуем матрицу в красивый вид
    for i in range(n):
        for j in range(n):
            while len(str(matr[i][j])) < (len(str(a))):
                matr[i][j] = " " + str(matr[i][j])
            print(matr[i][j], end=" ")
        print()


ulitka(11)
