def subtraction(a, b):
    if type(a) in [list, tuple]:
        return type(a)([x for x in a if x not in b])
    else:
        return a - b
    

s = eval(input())
print(subtraction(*s))