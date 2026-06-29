'''
*****
*  *
* *
**
*
'''
n = int(input("Enter a num: "))
for i in range(1,n+1):
    print("*",end="")
for k in range(1,n):
    print()
    for j in range(n,0,-1):
        if j==n or j==k:
            print("*",end="")
        else:
            print(" ",end="")