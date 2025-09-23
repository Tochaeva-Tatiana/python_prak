arr = eval(input())
first = arr[0]
for i in arr:
    if i % 2 == 1:
        print(i)
        break
else:
    print(first)