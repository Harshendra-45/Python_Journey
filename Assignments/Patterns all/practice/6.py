n = int(input("Enter a no: "))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print("*",end="")
    for k in range(0,i*2-2):
        print(" ",end="")
    for l in range(n,i-1,-1):
        print("*",end="")
    print()
for z in range(1,n+1):
    for j in range(1,z+1):
        print("*",end="")
    for k in range(n*2-2*z,0,-1):
        print(" ",end="")
    for l in range(1,z+1):
        print("*",end="")
    print()
    