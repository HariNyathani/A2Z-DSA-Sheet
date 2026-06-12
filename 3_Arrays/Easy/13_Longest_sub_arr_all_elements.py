def longest(arr,k):
    prefix_sum = {0:-1}
    current_sum = 0
    max_length = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        rem = current_sum - k

        if rem in prefix_sum:
            length = right - prefix_sum[rem]
            max_length = max(max_length, length)

        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = right

    return max_length

arr = [1, -1, 5, -2, 3]
print(longest(arr,3))
