class Vowel:
    __slots__ = ("a", "e", "i", "o", "u", "y", "_filled")

    answer = 42

    def __init__(self, **kwargs):
        self._filled = {slot: False for slot in ("a", "e", "i", "o", "u", "y")}
        for k, v in kwargs.items():
            if k not in self.__slots__:
                raise AttributeError("invalid slot: " + k)
            setattr(self, k, v)

    def __setattr__(self, name, value):
        if name == "full":
            return
        if name == "answer":
            raise AttributeError("answer is read-only")
        if name in self.__slots__:
            object.__setattr__(self, name, value)
            if name != "_filled":
                self._filled[name] = True
        else:
            raise AttributeError("not a slot")

    def __getattr__(self, name):
        if name == "full":
            return all(self._filled.values())
        if name in self.__slots__:
            if not self._filled[name]:
                raise AttributeError("slot not set: " + name)
            return object.__getattribute__(self, name)
        raise AttributeError("no such attribute")

    def __str__(self):
        parts = []
        for k in ("a", "e", "i", "o", "u", "y"):
            if self._filled[k]:
                parts.append(f"{k}: {getattr(self, k)}")
        return ", ".join(parts)


import sys
exec(sys.stdin.read())