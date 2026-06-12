def union_arrays(arrA, arrB):
    i = 0
    j = 0
    n = len(arrA)
    m = len(arrB)
    temp_arr = []
    while i < n and j < m:
        if arrA[i] < arrB[j]:
            if len(temp_arr) == 0 or temp_arr[-1] != arrA[i]:
                temp_arr.append(arrA[i]) 
            i += 1
        elif arrB[j] < arrA[i]:
            if len(temp_arr) == 0 or temp_arr[-1] != arrB[j]:
                temp_arr.append(arrB[j])
            j += 1
        else:
            if len(temp_arr) == 0 or temp_arr[-1] != arrA[i]:
                temp_arr.append(arrA[i])
            i += 1
            j += 1
    while i < n:
        if len(temp_arr) == 0 or temp_arr[-1] != arrA[i]:
            temp_arr.append(arrA[i])
        i += 1
    while j < m:
        if len(temp_arr) == 0 or temp_arr[-1] != arrB[j]:
            temp_arr.append(arrB[j])
        j += 1
    return temp_arr

arrA = [1, 1, 2, 3, 4, 5]
arrB = [1, 1, 2, 3, 4, 5]
print(union_arrays(arrA, arrB))

