'''
123456789
 1+++++7
  1+++5
   1+3
    1
'''
n = int(input("Enter a no: "))
for a in range(1,n*2):
    print(a,end="")

for i in range(1,n):
    print()
    p =2*n-2*i-1
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,p+1):
        if j==1 or j==p:
            print(j,end="")
        else:
            print("+",end="")
    