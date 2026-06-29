'''
    X
   X X
  X _ X
 X _ _ X
X X X X X

'''
n = int(input("Enter a no: "))
for i in range(1,n):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        if  k==1 or k==i:
            print("X ",end="")
        else:
            print("_ ",end="")
    print()
for z in range(1,n+1):
    print("X",end=" ")