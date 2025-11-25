class C(metaclass=sole):
    pass
class D(C): pass
class E(C, int): pass