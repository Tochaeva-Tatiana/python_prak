import sys

lines = [line.rstrip("\n") for line in sys.stdin]
H = len(lines)
W = len(lines[0])

inside = [list(row[1:-1]) for row in lines[1:-1]]
h = len(inside)
w = len(inside[0])

all_cells = h * w
gas = sum(row.count(".") for row in inside)
liq = sum(row.count("~") for row in inside)

flat = []
for r in range(h):
    for c in range(w):
        flat.append(inside[r][c])

flat_sorted = ["." ] * gas + ["~"] * liq

filled = []
k = 0
for r in range(h):
    row = []
    for c in range(w):
        row.append(flat_sorted[k])
        k += 1
    filled.append(row)

rot = [[""] * h for _ in range(w)]

for r in range(h):
    for c in range(w):
        rot[c][h - 1 - r] = filled[r][c]

H2 = len(rot)
W2 = len(rot[0])
out = []
out.append("#" * (W2 + 2))
for r in range(H2):
    out.append("#" + "".join(rot[r]) + "#")
out.append("#" * (W2 + 2))

for row in out:
    print(row)



L = 20
gas_bar = "." * round(L * gas / all_cells)
liq_bar = "~" * round(L * liq / all_cells)

gas_frac = f"{gas}/{all_cells}"
liq_frac = f"{liq}/{all_cells}"

maxlen = max(len(gas_frac), len(liq_frac))
gas_frac = gas_frac.rjust(maxlen)
liq_frac = liq_frac.rjust(maxlen)

print(f"{gas_bar.ljust(L)} {gas_frac}")
print(f"{liq_bar.ljust(L)} {liq_frac}")
