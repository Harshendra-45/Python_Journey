'''
    1
   1*1
  1***1
 1*****1
111111111
'''
n = int(input("Enter a no: "))
for i in range(1,n):
    p = i*2-1
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,p+1):
        if k==1 or k==p:
            print(1,end="")
        else:
            print("*",end="")
    print()
for a in range(1,2*n):
    print(1,end="")