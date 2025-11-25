import inspect

class A:
    a : int
    def __init__(self, val):
        if isinstance(val, inspect.get_annotations(self.__class__)['a']):
            self.a = val
        else:
            raise TypeError("aaa")
        
