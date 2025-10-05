def pareto(*pairs):
    res = list()
    for a in pairs:
        f = False
        for b in pairs:
            if a[0] <= b[0] and a[1] <= b[1] and (a[0] < b[0] or a[1] < b[1]):
                f = True
                break
        if not f:
            res.append(a)
    print(tuple(res))


s = eval(input())
pareto(*s)