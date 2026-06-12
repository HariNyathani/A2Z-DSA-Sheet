def Major_ele(nums):
  candidate = 0
  count = 0
  for num in nums:
    if count == 0:
      candidate = num
      count += 1
    elif num == candidate:
      count += 1
    else:
      count -= 1
  return candidate


arr = [9, 2, 9, 9, 5, 9, 1]
print(Major_ele(arr))
