'''
1
22
3 3
4  4
55555
'''
n = int(input("Enter a num: "))
i = 1
while i<=n-1:
    j = 1
    while j<=i:
        if j==1 or i==j:
            print(i,end="")
        else:
            print(" ",end="")
        j+=1
    i+=1
    print()
for i in range(1,n+1):
        print(n,end="")
        