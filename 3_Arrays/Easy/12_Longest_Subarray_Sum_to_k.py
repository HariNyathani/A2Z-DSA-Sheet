def longest(arr, k):
    left = 0
    current_sum = 0
    max_len = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum > k:
            current_sum -= arr[left]
            left += 1

        if current_sum == k:
            max_len = max(max_len, right-left+1)
        
    return max_len

arr = [1,2,3,1,1,1,1]
print(longest(arr,3))
            
