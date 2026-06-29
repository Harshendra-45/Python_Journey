'''
    A
   B B
  C  C
 D    D
EEEEEEEEE
'''
n = int(input("Enter a no: "))
ch=65
for i in range(1,n):
    p=2*i-1
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,p+1):
        if k==1 or k==p:
            print(chr(ch),end="")
        else:
            print(" ",end="")
        
    print()
    ch+=1
for a in range(1,n*2):
    print(chr(ch),end="")