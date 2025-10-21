def walk2d():
    x = y = 0
    while True:
        (dx, dy) = yield (x, y)
        x += dx
        y += dy


s = walk2d()

print(s)
print(s.send((3, 5)))
print(s.send((1, 1)))
print(s.send((2, 2)))
