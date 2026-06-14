def matrix(nums):
  m = len(nums)
  n = len(nums[0])
  row_tracker = [False] * m
  col_tracker = [False] * n
  for r in range(m):
    for c in range(n):
      if nums[r][c] == 0:
        row_tracker[r] = True
        col_tracker[c] = True
    
  for r in range(m):
    for c in range(n):
      if row_tracker[r] == True or col_tracker[c] == True:
        nums[r][c] = 0

  return nums

nums = [[1, 1, 1], [0, 1, 1], [1, 1, 1]]
matrix(nums)
