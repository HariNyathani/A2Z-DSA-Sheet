for i in range(1,5):
    for j in range(i):
        print(j+1,end="")
    for k in range(8-2*i):
        print(" ", end = "")
    for l in range(i):
        print(i-l, end = "")
    print()