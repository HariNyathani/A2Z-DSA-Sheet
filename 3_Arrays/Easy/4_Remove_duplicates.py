arr = [1, 1, 2, 2, 2, 3, 3]
def remove(arr):
    i = 0
    j = 1
    while j < len(arr):
        if arr[i] < arr[j]:
            i += 1
            arr[i] = arr[j]
            j += 1
        else:
            j += 1
    return arr

print(remove(arr)) 
