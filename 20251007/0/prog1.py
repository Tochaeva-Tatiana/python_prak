import decimal
import fractions

def mult(x, y, Type):
    return Type(x) * Type(y)

for i in (float, decimal.Decimal, fractions.Fraction):
    print(mult("1.323", "0.7578", i))