class Omnibus:
    counters = {}    # имя атрибута → сколько объектов имели этот атрибут

    def __setattr__(self, name, value):
        if name.startswith("_"):
            return super().__setattr__(name, value)

        # Если у объекта ещё не было этого атрибута → увеличиваем счётчик
        if name not in self.__dict__:
            Omnibus.counters[name] = Omnibus.counters.get(name, 0) + 1

        # Значение не хранится по смыслу — любой объект использует сам факт наличия
        self.__dict__[name] = True

    def __getattr__(self, name):
        # Чтение: возвращаем количество объектов, имеющих этот атрибут
        return Omnibus.counters.get(name, 0)

    def __delattr__(self, name):
        # Если объект имел этот атрибут — уменьшаем счётчик
        if name in self.__dict__:
            del self.__dict__[name]
            Omnibus.counters[name] -= 1
            if Omnibus.counters[name] == 0:
                del Omnibus.counters[name]


a, b, c = Omnibus(), Omnibus(), Omnibus()
del a.random
a.i = a.j = a.k = True
b.j = b.k = b.n = False
c.k = c.n = c.m = hex
print(a.i, a.j, a.k, b.j, b.k, b.n, c.k, c.n, c.m)
del a.k, b.n, c.m
print(a.i, a.j, b.j, b.k, c.k, c.n)
del a.k, c.m
print(a.i, a.j, b.j, b.k, c.k, c.n)
a.k = b.i = c.m = 777
print(a.i, a.j, a.k, b.j, b.k, c.k, c.n, c.m)