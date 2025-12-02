def subr():
    x = yield "Wait for x"
    y = yield f"Wait for y ({x=})"
    return x, y

def task():
    while True:
        value = yield from subr()
        _ = yield value

core = task()
print(next(core))
for i in range(8):
    print(core.send(i))