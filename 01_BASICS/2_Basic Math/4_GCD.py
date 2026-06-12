A = int(input("Enter a numbebr : "))
B = int(input("Enter a numbebr : "))

while A > 0 and B > 0:
    A , B = B , A%B
    
print(A)
