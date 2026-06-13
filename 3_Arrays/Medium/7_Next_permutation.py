def next_permutation(nums):
    n = len(nums)
    break_index = -1

    ### 1. Find out break point index (scan right-to-left)
    # We stop at index 1 so that i-1 never goes below index 0
    for i in range(n - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            break_index = i - 1
            break

    ### Edge Case: If no break point exists, the array is entirely descending (like [3, 2, 1])
    if break_index == -1:
        nums.reverse()
        return nums

    ### 2. Swap the elements
    # FIXED: Scanning from the back, the first element greater than nums[break_index]
    # is mathematically guaranteed to be the tightest/smallest candidate.
    for i in range(n - 1, break_index, -1):
        if nums[i] > nums[break_index]:
            nums[break_index], nums[i] = nums[i], nums[break_index]
            break

    ### 3. Arrange suffix elements in ascending order
    # FIXED: Reversing the descending suffix in-place using two pointers
    # instead of slicing with .sort() which returns None.
    left = break_index + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


arr = [2, 3, 6, 5, 4, 1]
print(next_permutation(arr))
