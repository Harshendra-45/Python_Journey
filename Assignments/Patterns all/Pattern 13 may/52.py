'''
12345
 1__4
  1_3
   12
    1
'''
n = int(input("Enter a num: "))
for num in range(1,n+1):
    print(num,end="")

for i in range(1,n):
    print()
    for j in range(0,i):
        print(" ",end="")
    for k in range(1,n+1-i):
        if k==1 or k==n-i:
            print(k, end="")
        else:
            print("_",end="")
   