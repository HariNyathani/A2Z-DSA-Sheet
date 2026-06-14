def matrix_rotate_90(matrix):
  n = len(matrix)
  for r in range(n):
    for c in range(r, n):
      matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
  for r in range(n):
    matrix[r].reverse()

  return matrix

nums = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

matrix_rotate_90(nums)
