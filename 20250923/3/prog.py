line = eval(input())
n = len(line)
matr1 = list()
matr2 = list()
matr3 = [[0] * n for i in range(n)]
matr1.append(line)
for i in range(n - 1):
    matr1.append(eval(input()))

for i in range(n):
    matr2.append(eval(input()))

for i in range(n):
    for j in range(n):
        for k in range(n):
            matr3[i][j] += matr1[i][k] * matr2[k][j]
for i in matr3:
    print(*i, sep=',')

