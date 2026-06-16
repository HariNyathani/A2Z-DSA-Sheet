def sub_array_sum(nums, k):
  prefix_map = {0:1}
  current_sum = 0
  rem = 0
  count = 0
  for i in range(len(nums)):
    current_sum += nums[i]
    rem = current_sum - k
    if rem in prefix_map:
      count += prefix_map[rem]
    if current_sum in prefix_map:
      prefix_map[current_sum] += 1
    else:
      prefix_map[current_sum] = 1
  return count

nums = [1,1,1]
sub_array_sum(nums,2)
