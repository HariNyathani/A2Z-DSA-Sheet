def Max_ones(arr):
    current_streak = 0
    maximum_streak = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            current_streak += 1
            maximum_streak = max(current_streak, maximum_streak)
        else:
            current_streak = 0
    return maximum_streak


arr = [1, 1, 0, 1, 1, 1]
print(Max_ones(arr))