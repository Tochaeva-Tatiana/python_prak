class ctype(type):
    @classmethod
    def __prepare__(metacls, name, parents, **kwds):
        print("PREPARE", name, parents, kwds)
        return super().__prepare__(name, parents, **kwds)

    def __init__(cls, name, parents, namespace, **kwds):
        print("INIT", name, parents, namespace, kwds)
        return super().__init__(name, parents, namespace)
    
    def __new__(metacls, name, parents, namespace, **kwds):
        print("NEW", metacls, name, parents, namespace, kwds)
        return super().__new__(metacls, name, parents, namespace)
    
    def __call__(cls, *args, **kwargs):
        print("CALL", cls, args, kwargs)
        return super().__call__(*args, **kwargs)
    
    