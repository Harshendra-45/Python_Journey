n=int(input("N"))
i=1
while i<=n:
    print()
    j=1
    while j<=n*2-1:
        if i==1 or i==n or j==1 or j==n*2-1:
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    i=i+1