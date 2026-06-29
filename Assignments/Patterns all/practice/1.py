k = int(input("Enter a no: "))
for b in range(1,k+1):
    print()
    for c in range(1,k-b+1):
        print(" ",end="")
    for d in range(1,2*b):
        print("*",end="")
    for e in range(1,k-b+1):
        print(" ",end="")
    
for i in range(1,k+1):
    print()
    #space
    for h in range(1,i):
        print(" ",end="")
    #stars
    for j in range((2*k)-2*i+1,0,-1):
        print("*",end="")

    #space2
    for a in range(1,i):
        print(" ",end="")
    