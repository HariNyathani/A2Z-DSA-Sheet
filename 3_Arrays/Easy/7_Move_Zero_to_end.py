def move_zero(arr):
    i = 0  # Anchor
    for j in range(len(arr)):  # Scout
        if arr[j] != 0:  # If Scout finds ANY non-zero number...
            arr[i], arr[j] = arr[j], arr[i]  # ...Swap it with the Anchor!
            i += 1  # Move Anchor up one spot
    return arr
# arr = [1,0,2,0,3]
arr = [5,6]
print(move_zero(arr))
