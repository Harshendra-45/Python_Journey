'''
ABCDE
ABCD
ABC
AB
A
'''
n = int(input("Enter a num: "))
i = 1

while i<=n:
    k = 65
    j = n
    while j>=i:
        print(chr(k),end="")
        k+=1
        j-=1
    i+=1
    
    print()