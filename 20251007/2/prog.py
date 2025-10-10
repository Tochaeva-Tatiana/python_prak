import math

data = input().split()
W = int(data[0])
H = int(data[1])
A = float(data[2])
B = float(data[3])
func_str = ' '.join(data[4:])

screen = [[' '] * W for _ in range(H)]

# Вычисляем значения функции для всех столбцов
values = []
for col in range(W):
    x = A + col * (B - A) / (W - 1)
    y = eval(func_str, {'x': x, 'math': math})
    values.append(y)

y_min = min(values)
y_max = max(values)

if y_min == y_max:
    y_min -= 1
    y_max += 1

# Рисуем только точки (без соединения линиями)
for col in range(W):
    y = values[col]
    # Преобразуем Y в координату строки (0 - верх, H-1 - низ)
    row = int((y_max - y) * (H - 1) / (y_max - y_min))
    
    if 0 <= row < H:
        screen[row][col] = '*'

print("\n".join("".join(row) for row in screen))