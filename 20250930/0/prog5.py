def MINF(*funcs):
    def fun(x):
        return min([f(x) for f in funcs])
    return fun