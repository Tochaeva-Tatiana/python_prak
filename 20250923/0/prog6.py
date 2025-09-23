n = int(input())
arr = [i for i in range(n) if '3' not in str(i) and i % 2 == 0]
print(arr)