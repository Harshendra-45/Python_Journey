'''
a
bc
d f
g  j
klmno
'''
n = int(input("Enter a num: "))
i = 1
ch = 97
while i<=n-1:
    j = 1
    while j<=i:
        if i==1 or j==i or j==1:
            print(chr(ch),end="")
        else:
            print(" ",end="")
        j+=1
        ch+=1
    i+=1
    print()
for i in range(1,n+1):
    print(chr(ch),end="")
    ch+=1