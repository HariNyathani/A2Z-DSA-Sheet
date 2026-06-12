def single(arr):
    a = arr[0]
    for i in range(1,len(arr)):
        a ^= arr[i]
    return a

arr = [4, 1, 2, 1, 2]
print(single(arr))
