def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_arr(arr, k):
    n = len(arr) 
    if n <= 1 or k == 0:
        return arr
    k = k % n
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

    return arr

arr = [1,2,3,4,5,6,7]
k = int(input("Enter an integer"))
rotated_array = rotate_arr(arr,k)
print(rotated_array)
