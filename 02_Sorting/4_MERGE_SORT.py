def merge(arr1, arr2):
    left = 0
    right = 0
    arr = []
    while left < len(arr1) and right < len(arr2):
        if arr1[left] < arr2[right]:
            arr.append(arr1[left])
            left += 1
        else: 
            arr.append(arr2[right])
            right += 1
    
    while left < len(arr1):
        arr.append(arr1[left])
        left += 1
    while right < len(arr2):
        arr.append(arr2[right])
        right += 1
    
    return arr

def merge_sort(arr):
    # 1. THE BASE CASE
    # If the array is 1 element (or empty), it is already sorted. Return it!
    if len(arr) <= 1:
        return arr

    # 2. THE SPLIT
    # Find the middle and slice the array into two new temporary arrays
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 3. THE RECURSIVE LEAP
    # We pause here! We throw the left half back into merge_sort to be split again.
    # We save whatever fully sorted array comes back as 'sorted_left'
    sorted_left = merge_sort(left_half)
    
    # Once the entire left side is fully sorted, we do the same to the right side
    sorted_right = merge_sort(right_half)

    # 4. THE CONQUER
    # Both halves are now perfectly sorted. Feed them into the helper function 
    return merge(sorted_left, sorted_right)

sorted_arr = merge_sort([4,3,2,1])
print(sorted_arr)