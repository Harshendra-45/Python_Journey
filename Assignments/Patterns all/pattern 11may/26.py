n= int(input("Enter number = "))
i=1
while i<=n:
    print()
    j=1
    while j<=n:
        if i==j or j==1 or i==n:
            print(j,end="")
        else:
            print(" ",end="")
        j+=1
    i+=1
    