class Num:
    def __set_name__(self, owner, name):
        self.name = "_" + name 

    def __get__(self, obj, owner):
        if obj is None:
            return self
        return getattr(obj, self.name, 0)

    def __set__(self, obj, value):
        if hasattr(value, "real"):
            setattr(obj, self.name, value.real)
        elif hasattr(value, "__len__"):
            setattr(obj, self.name, len(value))
        else:
            setattr(obj, self.name, value)

import sys
exec(sys.stdin.read())