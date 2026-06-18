### Pascal triangle - leetcode 118
def pascal(numRows):
  result_arr = []
  for i in range(numRows):
    row = []
    for j in range(i + 1):
      if j == 0 or j == i:
        row.append(1)
      else:
        row.append(result_arr[i -  1][j - 1] + result_arr[i - 1][j])
    result_arr.append(row)
  return result_arr

numRows = 5
pascal(numRows)
