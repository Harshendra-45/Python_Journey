'''
EEEEE
DDDD
CCC
BB
A
'''

n = int(input("Enter a num: "))
i = 1
k = 64+n
while i<=n:
    
    j = n
    while j>=i:
        print(chr(k),end="")
        
        j-=1
    i+=1
    k-=1
    print()