s = input().split()
while s:

    match s:
        case ["mov", str(a), str(b)]:
            print(f"moving {a} to {b}")
        case ["push" | "pop" as p, *reglist]:
            print(f"{p}ing", *reglist)
        case [str(a), str(b)]:
            print(f"making {a} with {b}")
        case _:
            print("Parse error")

    s = input().split()
