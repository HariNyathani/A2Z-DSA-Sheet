### Just a naive brute force

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result_arr = []
        for i in range(rowIndex + 1):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(result_arr[i -  1][j - 1] + result_arr[i - 1][j])
            result_arr.append(row)
        return result_arr[-1]

### Will come back tomorrow and do optimal for this question
