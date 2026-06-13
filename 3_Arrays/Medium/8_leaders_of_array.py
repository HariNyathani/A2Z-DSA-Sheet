def leaders(nums):
  max_from_right = nums[-1]
  ans = []
  ans.append(max_from_right)
  for i in range(len(nums) -2, -1, -1):
    if nums[i] > max_from_right:
      ans.append(nums[i])
      max_from_right = nums[i]
  ans.reverse()
  return ans

nums = [10, 22, 12, 3, 0, 6]
leaders(nums)

