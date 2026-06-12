arr = list(map(int, input().split()))
l = len(arr)

for i in range(0,l):
    for j in range(l - i - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
