'''
ABCDE
A  D
A C
AB
A
'''
n = int(input("Enter a num: "))
i = 1
ch = 65
for h in range(1,n+1):
    print(chr(ch),end="")
    ch+=1
while i<n:
    print()
    k = 65
    j = n-1
    while j>=i:
        if j==n-1 or j==i:
            print(chr(k),end="")
        else:
            print(" ",end="")
        k+=1
        j-=1
    i+=1
    
    