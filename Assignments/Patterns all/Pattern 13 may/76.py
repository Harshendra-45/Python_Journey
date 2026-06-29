'''
x
xx
xxx
xxxx
xxx
xx
x
'''
n = int(input("Enter a num: "))
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        print("x",end="")
    
for k in range(1,n):
    print()
    for j in range(n-1,k-1,-1):
        print("x",end="")
