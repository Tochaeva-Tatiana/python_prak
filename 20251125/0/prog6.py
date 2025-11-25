
class A:
    def __init__(self, s):
        self.a, self.b, self.c = s.split()


a = A(input())
s2 = input()
while s2:

    match s2.split():
        case [a.a, *args]:
            print(1)
        case [a.b]:
            print(2)
        case [a.c, *args, a.b]:
            print(3)

    s2 = input()


