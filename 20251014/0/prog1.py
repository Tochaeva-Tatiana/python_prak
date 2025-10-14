from string import ascii_lowercase
from timeit import Timer

def f(s):
    set_gl = set('aouei')
    set_so = set(ascii_lowercase) - set_gl

    return (len(s & set_gl), len(s & set_so))

s = set(input())
t = Timer('f(s)', globals=globals())
res = t.autorange()

print(res)

