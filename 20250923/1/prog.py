M, N = eval(input())
print([i for i in range(M, N+1) if len([j for j in range(1, int(i**(1/2))+1) if i % j == 0]) == 1])