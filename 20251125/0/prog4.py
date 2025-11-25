match eval(input()):
    case "QWE":
        print("QWE!")
    case int(n) if n > 0:
        print("int > 0", n)
    case int(n):
        print("int", n)
    case (0, *tail):
        print("Zero tuple", tail)
    case _:
        print("dddddddd")