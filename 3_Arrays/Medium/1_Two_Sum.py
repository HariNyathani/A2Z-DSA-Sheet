def two_sum(arr, target):
    seen = {}
    for i in range(len(arr)):
        component = target - arr[i]
        if component in seen:
            return [seen[component],i]
        else:
            seen[arr[i]] = i



arr = [2,3,4]
target = 5
print(two_sum(arr,target))



