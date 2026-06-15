def spiral_matrix(matrix):
  m = len(matrix)
  n = len(matrix[0])
  top = 0
  bottom = m - 1
  left = 0
  right = n - 1
  ans = []
  while left <= right and top <= bottom:
    for col in range(left, right + 1):
      ans.append(matrix[top][col])
    top += 1
    for row in range(top, bottom + 1):
      ans.append(matrix[row][right])
    right -= 1
    if top <= bottom:
      for col in range(right, left - 1, -1):
        ans.append(matrix[bottom][col])
      bottom -= 1
    if left <= right:
      for row in range(bottom, top - 1, -1):
        ans.append(matrix[row][left])
      left += 1
  return ans

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
spiral_matrix(matrix)
