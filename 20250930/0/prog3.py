def f(n):
    print(n)
    if n != 0:
        return f(n-1)
    
f(6)