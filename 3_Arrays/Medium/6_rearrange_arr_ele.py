### Optimal approach, even though its optimal it takes O(N) Space as we need to entirely rearrage elements of an array

def rearrange(nums):
  pos_ind = 0
  neg_ind = 1
  ans = [0] * len(nums)
  for i in nums:
    if i > 0:
      ans[pos_ind] = i
      pos_ind += 2
    else:
      ans[neg_ind] = i
      neg_ind += 2

  return ans

nums = [3, 1, -2, -5, 2, -4]
rearrange(nums)
