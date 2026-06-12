n = int(input("Enter a numbebr : "))
original = n
rev = 0
if n < 0:
    print(f"{n} is not a palindrome")

while n > 0:
    rev = n % 10 + rev*10
    n = n // 10

if original > 0:
    if original == rev:
        print(f"{original} is a palindrome")
    else:
        print(f"{original} is not a palindrome")