'''
A B C D E
 A B C D
  A B C
   A B
    A

'''

n = int(input("Enter a no: "))

for i in range(1,n+1):
    ch=65
    for k in range(1,i):
        print(" ",end="")
    for j in range(n,i-1,-1):
        print(chr(ch),end=" ")
        ch+=1
    print()