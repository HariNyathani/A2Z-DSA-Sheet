arr = [2, 4, 5, 4, 6]
def sort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print(sort(arr))
