
f_line = input()
f_line = list(eval(f_line))
matrix = []
matrix.append(f_line)

lenght = len(f_line)

for i in range(lenght - 1):
    line = input()
    line = list(eval(line))
    matrix.append(line)

if any([len(line) != len(matrix) for line in matrix]):
    print('nonono')
else:


    for j in range(lenght):
        for i in range(j + 1, lenght):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in matrix:
        print(*i)
