from math import *

functions = {"quit": (["fmt"], None)}
defined_count = 1
line_count = 0

while True:
    line = input()
    line_count += 1


    if line.startswith(':'):
        parts = line.split()
        fname = parts[0][1:]
        params = parts[1:-1]
        expr = parts[-1]
        functions[fname] = (params, expr)
        defined_count += 1
        continue

    space = line.find(' ')
    if space == -1:
        fname = line
        rest = ""
    else:
        fname = line[:space]
        rest = line[space+1:]

    if fname == "quit":
        fmt = rest.strip()
        print(fmt.format(defined_count, line_count))
        break

    params, expr = functions[fname]
    argc = len(params)

    args = []

    if argc == 0:
        pass

    elif argc == 1:
        arg = eval(rest.strip())
        args.append(arg)

    else:
        tokens = rest.split()
        for tok in tokens:
            args.append(eval(tok))

    local_env = {p: a for p, a in zip(params, args)}

    result = eval(expr, globals(), local_env)
    print(result)
