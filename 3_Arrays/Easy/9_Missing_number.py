#Optimal approach
def missing_num(arr):
    n = len(arr) + 1
    actual_sum = sum(arr)
    expected_sum = (n*(n+1))//2
    missing_number = expected_sum - actual_sum
    return missing_number
arr = [5, 2, 1, 4]
print(missing_num(arr))

# Only works on Sorted arrays, NOT recommended
arr = [1, 2, 4, 5]

def missing_number(arr):
    if arr[0] != 1:
        return 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            i += 1
        else:
            return arr[i] - 1
        
print(missing_number(arr))

