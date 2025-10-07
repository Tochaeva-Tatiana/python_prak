
def enum(N, one):
    pred = one
    s = one
    for i in range(1, N):
        pred *= i
        s += one/pred
    return s


