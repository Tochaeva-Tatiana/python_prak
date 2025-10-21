import itertools

def repeater(seq, n):
    for i in seq:
        yield from itertools.repeat(i, n)


print(list(repeater("dfg", 4)))
        