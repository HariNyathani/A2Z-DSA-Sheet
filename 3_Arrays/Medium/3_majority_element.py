def majority(nums):
    nums.sort()
    return nums[len(nums)//2]

nums = [9, 2, 9, 9, 5, 9, 1]
print(majority(nums))