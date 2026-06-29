'''
12345
1234
123
12
1
'''
n = int(input("Enter a num: "))
for i in range(1,n+1):
    b = 1
    for j in range(n+1,i,-1):
        print(b,end="")
        b+=1
    print()