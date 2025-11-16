from collections import UserString

class DivStr(UserString):
    def __init__(self, seq=""):
        super().__init__(seq)

    def __floordiv__(self, n):
        """a // n -> iterator of n substrings of equal max size"""
        if n <= 0:
            raise ValueError("// n: n must be positive")

        L = len(self.data)
        chunk = L // n  # minimal equal size
        res = [self.data[i*chunk:(i+1)*chunk] for i in range(n)]
        return iter(map(DivStr, res))

    def __mod__(self, n):
        """a % n -> remainder substring"""
        if n <= 0:
            raise ValueError("% n: n must be positive")

        L = len(self.data)
        chunk = L // n
        tail = self.data[chunk*n:]
        return DivStr(tail)

    def __add__(self, other):
        return DivStr(self.data + str(other))


import sys
exec(sys.stdin.read())