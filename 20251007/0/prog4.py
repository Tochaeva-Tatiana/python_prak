from math import sin

W, H = eval(input())
A, B = eval(input())
screen = [['.']*W for i in range(H)]

for line in range(0, W):
    x = A + line * (B-A) / (W - 1)
    y = sin(x)
    k = round((y + 1) * (H - 1) / 2)
    screen[H - k - 1][line] = "*"

print("\n".join("".join(i)  for i in screen))