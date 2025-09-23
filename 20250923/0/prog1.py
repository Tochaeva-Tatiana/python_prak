arr_1 = [i for i in range(5, 16)]
arr_2 = [chr(ord('a') + i) for i in range(ord('k') - ord('a') + 1)]

arr_1[4:8] = arr_2[-5:]
print(arr_1, arr_2)
