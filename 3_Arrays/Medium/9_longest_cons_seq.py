def longestConsecutive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    longest_streak = 1

    for i in num_set:
        if i-1 not in num_set:
            current_num = i
            current_streak = 1
            while current_num + 1 in num_set:
                current_streak += 1
                current_num += 1

            if longest_streak < current_streak:
                longest_streak = current_streak

    return longest_streak

nums = [100, 4, 200, 1, 3, 2]  
longest_con_seq(nums)
