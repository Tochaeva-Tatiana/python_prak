def fib(m, n):
    a = b = 1
    seq = []
    for i in range(m + n):
        seq.append(a)
        a, b = b, a + b
    yield from seq[m : m + n]

import sys
exec(sys.stdin.read())