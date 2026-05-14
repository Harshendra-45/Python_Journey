'''
A
AB
A C
A  D
ABCDE

'''
n = int(input("Enter a num: "))
i = 1

while i<=n-1:
    ch = 65
    j = 1
    while j<=i:
        if j==1 or i==j:
            print(chr(ch),end="")
        else:
            print(" ",end="")
        j+=1
        ch+=1
    i+=1
    print()
ch = 65
for i in range(1,n+1):
    print(chr(ch),end="")
    ch+=1