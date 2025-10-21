def genf():
    s = i = 0
    while True:
        i += 1
        s += 1/(i**2)
        yield s


