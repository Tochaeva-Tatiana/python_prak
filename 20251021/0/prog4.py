def travel(n):
    for i in range(n):
        yield "по кочкам\n"
    return "и в яму"

s = travel(6)

print(*s)