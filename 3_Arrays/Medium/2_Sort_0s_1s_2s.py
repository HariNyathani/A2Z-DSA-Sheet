### DUTCH NATIONAL FLAG
class Solution():
    def Sort_arr(self,nums):
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:    #[1, 0, 0, 2, 1, 2, 0, 2]
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

        return nums

s = Solution()
arr = [1, 0, 0, 2, 1, 2, 0, 2]
print(s.Sort_arr(arr))

