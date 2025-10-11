import math

W, H, A, B, *expr_parts = input().split()
W = int(W)
H = int(H)
A = float(A)
B = float(B)
expr = " ".join(expr_parts)

screen = [[" "] * W for _ in range(H)]


def f(x):
    return eval(expr, {"x": x, **math.__dict__})


xs = [A + (B - A) * i / (W - 1) for i in range(W)]
ys = [f(x) for x in xs]

mn = min(ys)
mx = max(ys)


def scale(a, b, A, B, x):
    if a == b:
        return (A + B) / 2
    return A + (B - A) * (x - a) / (b - a)



for i in range(W):
    y = ys[i]
    row = int(round(scale(mn, mx, H - 1, 0, y)))
    screen[row][i] = "*"

    if i > 0:
        prev_row = int(round(scale(mn, mx, H - 1, 0, ys[i - 1])))
        r1, r2 = sorted([row, prev_row])
        for r in range(r1, r2 + 1):
            screen[r][i] = "*"


for row in screen:
    print("".join(row))
