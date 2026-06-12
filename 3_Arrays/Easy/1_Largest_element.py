#This is the most optimal approach
arr = [3,2,6,1]
a = arr[0]
for i in range(1, len(arr)):
    if a < arr[i]:
        a = arr[i]

print(a)

# Here bruteforce is by sorting and finding the last element as even the most efficient 
# merge sort time complexity is O(NlogN) while we did above with only N