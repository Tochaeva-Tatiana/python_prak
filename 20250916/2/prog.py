a = int(input())
sum_a = a

while sum_a <= 21:
    a = int(input())
    if a <= 0:
        print(a)
        break
    sum_a += a
else:
    print(sum_a)