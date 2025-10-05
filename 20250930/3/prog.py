from math import *

def Calc(f, g, h):
    def F(x):
        val_x = eval(f, globals(), {'x': x})
        val_y = eval(g, globals(), {'x': x})
        return eval(h, globals(), {'x': val_x, 'y': val_y})
    return F

funs, val = eval(input()), int(input())
F = Calc(*funs)
print(F(val))
