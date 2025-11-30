import math

lines = []

# ---------- ввод программы ----------
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

commands = []
labels = {}

# ---------- 1 проход: сбор команд и меток ----------
for line in lines:
    line = line.lstrip()
    if not line:
        continue

    if ":" in line:
        label, _, rest = line.partition(":")
        if label:
            labels[label] = len(commands)
        line = rest.strip()

    if not line:
        continue

    parts = line.split()
    commands.append(parts)

# ---------- проверка меток ----------
for cmd in commands:
    if len(cmd) == 4 and cmd[0].startswith("if"):
        if cmd[3] not in labels:
            raise SystemExit

# ---------- 2 проход: интерпретация ----------
vars = {}
pc = 0

def value(x):
    try:
        return float(x)
    except:
        return vars.get(x, 0.0)

while pc < len(commands):
    cmd = commands[pc]
    pc += 1

    match cmd:
        case ["stop"]:
            break

        case ["store", num, dst]:
            try:
                vars[dst] = float(num)
            except:
                vars[dst] = 0.0

        case ["add" | "sub" | "mul" | "div" as op, a, b, dst]:
            try:
                x, y = value(a), value(b)
                res = {
                    "add": x + y,
                    "sub": x - y,
                    "mul": x * y,
                    "div": x / y,
                }[op]
            except:
                res = math.inf
            vars[dst] = res

        case ["ifeq" | "ifne" | "ifgt" | "ifge" | "iflt" | "ifle" as op, a, b, lbl]:
            x, y = value(a), value(b)
            cond = {
                "ifeq": x == y,
                "ifne": x != y,
                "ifgt": x > y,
                "ifge": x >= y,
                "iflt": x < y,
                "ifle": x <= y,
            }[op]
            if cond:
                pc = labels[lbl]

        case ["out", x]:
            print(value(x))

        case _:
            pass
