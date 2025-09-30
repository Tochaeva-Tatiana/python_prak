def average(a, *lst):
    s = a + sum(lst)
    return s / (len(lst) + 1) 

print(average(1, 2, 3, 4, 5, 6, 7))