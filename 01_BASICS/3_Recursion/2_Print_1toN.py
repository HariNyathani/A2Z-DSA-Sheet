def numbers(n):
    if n == 0:
        return
    
    numbers(n-1)
    print(n)  

n = int(input())
numbers(n)