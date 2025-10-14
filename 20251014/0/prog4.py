# print(eval("a + b", {"b": 728, "a": 23}))

s = input()
a, b = eval(input())

print(eval(s, {"x": a, "y" : b}))
print(eval(s, {"y": a, "x" : b}))