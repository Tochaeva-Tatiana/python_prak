def subr():
    x = yield
    y = yield
    return [x,  y]

def task(num):
    res = []
    for i in range(num):
        res += yield from subr()
    return res

def loop(*tasks):
    queue, result = list(tasks), []
    print("Start:", *queue, sep="\n\t")
    for task in tasks:
        next(task)
    step = 0
    while queue:
        task = queue.pop(0)
        try:
            task.send(step)
        except StopIteration as ret:
            result.append((hex(id(task)), ret.value))
        else:
            queue.append(task)
        step += 1
    return result

print("Done:", *loop(task(7), task(2), task(5)), sep="\n\t")