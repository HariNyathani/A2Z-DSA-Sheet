n = int(input("Enter a number : "))
original = n
sum = 0
len_n = len(str(n))

while n>0:
    sum = (n%10)**len_n + sum
    n = n//10

if original == sum:
    print(f"{original} is an armstrong number.")
else:
    print(f"{original} is not an armstrong number.")
