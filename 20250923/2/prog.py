arr = eval(input())

arr = [(i, (i**2) % 100) for i in arr]
n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j][1] > arr[j + 1][1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print([i[0] for i in arr])