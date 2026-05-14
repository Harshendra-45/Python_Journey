'''
1
10
101
1010
10101
'''
n = int(input("Enter a num: "))
i = 1
while i<=n:
    j = 1
    while j<=i:
        if j%2!=0:
            print(1,end="")
        else:    
            print(0,end="")
        j+=1
    i+=1
    print()
