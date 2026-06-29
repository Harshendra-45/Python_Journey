'''
    5
   44
  333
 2222
11111
'''
n = int(input("Enter a num: "))
b = n
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(b,end="")
    print()
    b-=1

