from fractions import Fraction

def parse_rational(s):
    if '/' in s:
        parts = s.split('/')
        return Fraction(int(parts[0]), int(parts[1]))
    else:
        return Fraction(int(s))

def eval_polynomial(coeffs, x):
    result = Fraction(0)
    for coeff in coeffs:
        result = result * x + coeff
    return result

def check_solution(s, w, coeffs_A, coeffs_B):
    A_val = eval_polynomial(coeffs_A, s)
    B_val = eval_polynomial(coeffs_B, s)
    if B_val == 0:
        return False
    return A_val / B_val == w


data = input().split(', ')

s = parse_rational(data[0])
w = parse_rational(data[1])

deg_A = int(data[2])
coeffs_A = []
for i in range(deg_A + 1):
    coeffs_A.append(parse_rational(data[3 + i]))


deg_B = int(data[3 + deg_A + 1])
coeffs_B = []
start_index = 3 + deg_A + 2
for i in range(deg_B + 1):
    coeffs_B.append(parse_rational(data[start_index + i]))

result = check_solution(s, w, coeffs_A, coeffs_B)
print(result)
