arr = [10, 10, 5]
largest = arr[0]
second = 0
if len(arr) > 1:
    for i in range(1,len(arr)):
        if largest < arr[i]:
            second = largest
            largest = arr[i]
        else:
            if largest > arr[i] >= second:
                second = arr[i]
    print(second)
else:
    print("Array has only 1 element.")

