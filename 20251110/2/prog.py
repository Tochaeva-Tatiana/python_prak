class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass


def triangleSquare(s: str) -> float:
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except:
        raise InvalidInput()

    # проверка чисел
    try:
        x1, y1, x2, y2, x3, y3 = map(float, (x1, y1, x2, y2, x3, y3))
    except:
        raise BadTriangle()

    # площадь по формуле
    area = abs(
        x1*(y2 - y3) +
        x2*(y3 - y1) +
        x3*(y1 - y2)
    ) / 2

    if area == 0:
        raise BadTriangle()

    return area




while True:
    inp = input().strip()
    try:
        area = triangleSquare(inp)
    except InvalidInput:
        print("Invalid input")
        continue
    except BadTriangle:
        print("Not a triangle")
        continue
    else:
        print(f"{area:.2f}")
        break
