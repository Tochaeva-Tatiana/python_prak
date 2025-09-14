inp_arr = input()
inp_arr = inp_arr[1:-1]
arr = inp_arr.split(',')
arr = [int(i) for i in arr]
arr.sort()
print(', '.join([str(i) for i in arr]))
