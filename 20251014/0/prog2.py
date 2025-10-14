from collections import Counter
from timeit import Timer

def f(s):
    d = dict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

s = input().split()
t = Timer('f(s)', globals=globals())
print(t.autorange())

t2 = Timer('Counter(s)', globals=globals())
print(t2.autorange())
