N = int(input())
for i in range(N):
    print(f"{bin(i):0>{N-10}} = {hex(i): >{5}}")