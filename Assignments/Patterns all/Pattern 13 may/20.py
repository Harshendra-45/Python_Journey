'''
1
12
1 3
1  4
12345
'''
n = int(input("Enter a num: "))
i = 1
while i<=n-1:
    j = 1
    while j<=i:
        if j==1 or i==j:
            print(j,end="")
        else:
            print(" ",end="")
        j+=1
    i+=1
    print()
for k in range(1,n+1):
    print(k,end="")