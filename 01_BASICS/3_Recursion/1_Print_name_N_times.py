def name(n):
    if n == 0:
        return
    print("Ash born")
    name(n-1)

    
n = int(input())
name(n)