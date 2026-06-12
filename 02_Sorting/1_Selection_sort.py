arr = list(map(int,input().split()))
l = len(arr)

for i in range(l - 1): #0 - 5 
    mini = i  # 0,0
    for j in range(i+1, l): # 1,3
        if arr[i] > arr[j]: # 5 >  2
            if arr[mini] > arr[j]:
                mini = j
    arr[i], arr[mini] = arr[mini], arr[i]

print(arr)
