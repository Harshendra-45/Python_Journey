'''
A
BCD
EFGHI
JKLMNOP
'''
n = int(input("Enter a no: "))
i = 1
k = 1
ch = 65
while i<=n:
    j = 1
    while j<=k:
        print(chr(ch),end="")
        j+=1
        ch+=1
    print()
    i+=1
    k+=2
'''
#better approach without k    
n = int(input("Enter a no: "))
i = 1
ch = 65
while i<=n:
    j = 1
    while j<=2*i-1:
        print(chr(ch),end="")
        j+=1
        ch+=1
    print()
    i+=1
    '''
    
