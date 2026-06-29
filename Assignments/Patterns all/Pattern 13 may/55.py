'''
ABCDE
 ABCD
  ABC
   AB
    A
'''
n = int(input("Enter a no:"))
for i in range(1,n+1):
    
    ch=65
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n-i+2):
        print(chr(ch),end="")
        ch+=1
    print() 