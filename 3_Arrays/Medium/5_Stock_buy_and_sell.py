### Brute force

def stock(nums):
  max_profit = nums[1] - nums[0]
  for i in range(len(nums) - 1):
    for j in range(i+1, len(nums)):
      if max_profit < nums[j] - nums[i]:
        max_profit = nums[j] - nums[i]
  return max_profit

arr = [7, 1, 5, 3, 6, 4]
stock(arr)
