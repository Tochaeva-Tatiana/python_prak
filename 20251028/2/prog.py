class Triangle:
    def __init__(self, A, B, C):
        self.A = tuple(A)
        self.B = tuple(B)
        self.C = tuple(C)

    @staticmethod
    def _area2(A, B, C):
        return abs(
            (B[0] - A[0])*(C[1] - A[1]) -
            (B[1] - A[1])*(C[0] - A[0])
        )

    def __abs__(self):
        return Triangle._area2(self.A, self.B, self.C) / 2

    def __bool__(self):
        return abs(self) != 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    # точка внутри треугольника
    @staticmethod
    def _inside(P, A, B, C):
        area = Triangle._area2(A, B, C)
        a1 = Triangle._area2(P, B, C)
        a2 = Triangle._area2(A, P, C)
        a3 = Triangle._area2(A, B, P)
        return a1 + a2 + a3 == area

    def __contains__(self, other):
    # пустой треугольник — не содержит точек, но содержится везде
        if not other:
            return True
        if not self:
            return False

        # если "other" — точка
        if isinstance(other, tuple) and len(other) == 2:
            return Triangle._inside(other, self.A, self.B, self.C)

        # если "other" — треугольник
        return (
            Triangle._inside(other.A, self.A, self.B, self.C) and
            Triangle._inside(other.B, self.A, self.B, self.C) and
            Triangle._inside(other.C, self.A, self.B, self.C)
        )


    # пересечение треугольников через проверку сегментов и попадания точек
    @staticmethod
    def _segs_intersect(A, B, C, D):
        # стандартная проверка
        def orient(a, b, c):
            return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

        o1 = orient(A,B,C)
        o2 = orient(A,B,D)
        o3 = orient(C,D,A)
        o4 = orient(C,D,B)

        # пересечение
        if o1*o2 < 0 and o3*o4 < 0:
            return True

        return False

    def __and__(self, other):
        if not self or not other:
            return False

        S1 = [self.A, self.B, self.C]
        S2 = [other.A, other.B, other.C]

        # пересечение сторон
        for i in range(3):
            for j in range(3):
                if Triangle._segs_intersect(
                        S1[i], S1[(i+1)%3],
                        S2[j], S2[(j+1)%3]):
                    return True

        # один внутри другого
        if other.A in self:
            return True
        if self.A in other:
            return True

        return False


import sys
exec(sys.stdin.read())
