import sys



data = sys.stdin.buffer.read()


# Первый байт — количество частей
N = data[0]
tail = data[1:]
L = len(tail)

# На всякий случай: если N == 0, просто вернём вход как есть
if N == 0:
    sys.stdout.buffer.write(data)


parts = []
for i in range(N):
    start = L * i // N
    end = L * (i + 1) // N
    parts.append(tail[start:end])

# Лексикографическая сортировка байтовых строк
parts.sort()

result = bytes([N]) + b"".join(parts)
sys.stdout.buffer.write(result)



