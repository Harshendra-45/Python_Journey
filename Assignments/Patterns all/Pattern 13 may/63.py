'''
    A
   ABC
  ABCDE
 ABCDEEF
ABCDEFGHI
'''
n = int(input("Enter a no: "))
for i in range(1,n+1):
    ch = 65
    p=i*2-1
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,p+1):
        print(chr(ch),end="")
        ch+=1
    print()