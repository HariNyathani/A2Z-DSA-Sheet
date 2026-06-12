n = int(input("Enter a number : "))
divisors = []
for i in range(1, (n//2)+1):
    if n%i == 0:
        divisors.append(i)
divisors.append(n)

print(divisors)