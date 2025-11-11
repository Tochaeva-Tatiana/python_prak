
def istype(t):
    def mcdecor(f):
        def decor(*args):
            res = all([type(val) == t for val in args])
            if not res:
                raise TypeError
            return f(*args)
        return decor
    return mcdecor
    