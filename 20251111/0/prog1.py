def isint(f):
    def decor(*args):
        res = all([type(val) == int for val in args])
        if not res:
            raise TypeError
        return f(*args)
    return decor 

