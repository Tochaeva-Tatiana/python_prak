from fractions import Fraction

def parse_num(s):
    if "/" in s:
        return Fraction(s)
    else:
        return Fraction(int(s), 1)

def polyval(coeffs, x):
    r = x * 0
    for c in coeffs:
        r = r * x + c
    return r

def check_equation(s, w, degA, Acoeffs, degB, Bcoeffs):
    sx = s
    wx = w

    Aval = polyval(Acoeffs, sx)
    Bval = polyval(Bcoeffs, sx)

    if Bval == 0:
        return False

    return Aval / Bval == wx



data = input().replace(",", " ").split()

ptr = 0
s = parse_num(data[ptr]); ptr += 1
w = parse_num(data[ptr]); ptr += 1

degA = int(data[ptr]); ptr += 1
Acoeffs = [parse_num(data[ptr+i]) for i in range(degA+1)]
ptr += degA+1

degB = int(data[ptr]); ptr += 1
Bcoeffs = [parse_num(data[ptr+i]) for i in range(degB+1)]

print(check_equation(s, w, degA, Acoeffs, degB, Bcoeffs))
