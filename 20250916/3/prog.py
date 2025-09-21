n = int(input())
i = 0
while i <= 2:
    j = 0
    while j <= 2:
        mul = (n + i) * (n + j)
        print(n + i, '*', n + j, '=', end=' ')
        temp = mul
        sum_mul = 0
        while temp > 0:
            sum_mul += temp % 10
            temp //= 10

        if sum_mul == 6:
            print(":=)", end=' ')
        else:
            print(mul, end=' ')
        j += 1
    print()
    i+=1
        