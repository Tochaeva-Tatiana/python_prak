# Читаем вход и сразу считаем жидкость и газ
container = []
line = input().strip()
container.append(line)
liquid = line.count('~')
gas = line.count('.')
width = len(line)
height = 1

while True:
    line = input().strip()
    if line:
        container.append(line)
        liquid += line.count('~')
        gas += line.count('.')
        height += 1
    if line == len(line) * '#':
        break

# Поворачиваем контейнер
rotated = []
for i in range(width):
    new_row = ''
    for j in range(height-1, -1, -1):
        new_row += container[j][i]
    rotated.append(new_row)

# Перераспределяем жидкость и газ в повернутом контейнере
# В каждой колонке жидкость должна быть внизу, газ вверху
gas_len = gas
liquid_len = 0
new_rotated = []
for col in rotated:
    if col == height * '#':
        new_rotated.append(col)
    else:
        if gas_len >= height-2:
            new_rotated.append('#' + '.' * (height - 2) + '#')
            gas_len -= height-2
        else:
            new_rotated.append('#' + '~' * (height - 2) + '#')
            liquid_len += height-2


# Выводим повернутый контейнер
for row in new_rotated:
    print(row)

total = gas + liquid

print('.' * gas, f'{gas}/{total}')
print('~' * liquid, f'{liquid}/{total}')