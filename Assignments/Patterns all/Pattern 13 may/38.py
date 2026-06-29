'''
55555
4  4
3 3
22
1
'''
n = int(input("Enter a no: "))
p = n
for i in range(1,n+1):
    print(p,end="")
p-=1
i = 1

while i<=n:
    print()
    j = n-1
    while j>=i:
        if j==n-1 or j==i:
            print(p,end="")
        else:
            print(" ",end="")
        j-=1
    i+=1
    p-=1
