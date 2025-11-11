def istype(t):
    class Dec:
        def __init__(self, f):
            self.f = f

        def __call__(self, *args):
            res = all([type(val) == t for val in args])
            if not res:
                raise TypeError
            return self.f(*args)
    return Dec
