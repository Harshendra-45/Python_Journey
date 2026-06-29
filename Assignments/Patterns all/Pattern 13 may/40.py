'''
*
**
****
*******
***********
'''
n = int(input("Enter a no: "))
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print("*",end="")
    k+=i
    print()