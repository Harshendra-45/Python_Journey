'''
    *
   *_*
  *___* 
 *_____* 
*********
'''
n = int(input("Enter a no: "))
for i in range(1,n+1):
    p = i*2-1
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,p+1):
        if k==1 or k==p:
            print("*",end="")
        else:
            print("_",end="")
    print()