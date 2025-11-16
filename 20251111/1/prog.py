def objcount(cls):
    cls.counter = 0   # поле класса

    old_init = getattr(cls, "__init__", lambda self: None)
    old_del  = getattr(cls, "__del__", lambda self: None)

    def new_init(self, *args, **kwargs):
        cls.counter += 1
        old_init(self, *args, **kwargs)

    def new_del(self):
        cls.counter -= 1
        old_del(self)

    cls.__init__ = new_init
    cls.__del__  = new_del
    return cls




import sys
exec(sys.stdin.read())

