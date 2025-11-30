import types

class dump(type):
    def __new__(cls, name, bases, clsdict):
        for attr_name, attr_value in clsdict.items():
            if isinstance(attr_value, types.FunctionType):
                clsdict[attr_name] = cls._wrap_method(attr_value)
        return super().__new__(cls, name, bases, clsdict)

    @staticmethod
    def _wrap_method(method):
        def wrapper(*args, **kwargs):
            filtered_args = tuple(arg for arg in args if isinstance(arg, (str, int, float, bool)))
            filtered_kwargs = {k: v for k, v in kwargs.items() if isinstance(v, (str, int, float, bool))}
            print(f"{method.__name__}: {filtered_args}, {filtered_kwargs}")
            return method(*args, **kwargs)
        return wrapper

class TestClass(metaclass=dump):
        def __init__(self, x):
            self.x = x
        
        def add(self, y):
            return self.x + y
    
obj = TestClass(5)
result = obj.add(3)
print(result)