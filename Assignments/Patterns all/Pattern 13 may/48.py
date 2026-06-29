'''
    A
   AB
  A_C
 A__D
ABCDE
'''
n = int(input("Enter a num: "))
i = 1
while i<=n-1:
    j = 1
    while j<=n-i:
        print(" ",end="")
        j+=1
    k = 1
    ch = 65
    while k<=i:
        if k==1: 
            print(chr(ch),end="")
        elif k==i:
            print(chr(ch),end="")   
        else:
            print("_",end="")
        k+=1
        ch+=1
    i+=1
    print()
ch=65
for i in range(1,n+1):
    print(chr(ch),end="")
    ch+=1