'''
ABCDE
 A__D
  A_C
   AB
    A
'''
n = int(input("Enter a num: "))
ch=65
for a in range(1,n+1):
    print(chr(ch),end="")
    ch+=1
i = 1
while i<=n-1:
    print()
    ch=65
    j = 1
    while j<=i:
        print(" ",end="")
        j+=1
    k=1
    while k<=n-i:
        if k==1 or k==n-i:
            print(chr(ch),end="")
        else:
            print("_",end="")
        k+=1
        ch+=1
    i+=1
    