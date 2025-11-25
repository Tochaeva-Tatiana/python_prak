class Doubleton(type):
    _instance = None
    c = 0
    arr = []
    def __call__(cls, *args, **kw):
        if cls.c < 2:
            cls._instance = super().__call__(*args, **kw)
            cls.arr.append(cls._instance)
        res = cls.arr[cls.c % 2]
        cls.c += 1
        return res