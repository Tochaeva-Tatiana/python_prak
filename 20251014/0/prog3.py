s = input().split()
d = dict()
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(' '.join(list(d)))
