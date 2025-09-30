def den_adders(n):
    adders = []
    for i in range(n):
        def fun(x):
            return x + i
        adders.append(fun)
    return adders
