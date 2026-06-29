'''
    A
   AB 
  ABC
 ABCD
ABCDE
'''
n = int(input("Enter a num: "))
b = n

for i in range(1,n+1):
    ch = 65
    for j in range(1,n+1-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(chr(ch),end="")
        ch+=1
    print()
    b-=1
