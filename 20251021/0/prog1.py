def gen_1(n):
    s = 0
    for i in range(1, n+1):
        s += 1/(i**2)
        yield s

e = gen_1(100)
for i in range(100):
    print(next(e))