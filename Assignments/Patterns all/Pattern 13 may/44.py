'''
    1
   22
  333
 4444
55555
'''

n = int(input("Enter a num: "))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(i,end="")
    print()