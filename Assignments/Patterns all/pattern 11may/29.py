'''
    1 - - -
    - 2 - -
    - - 3 -
    - - - 4

'''
n = int(input("Enter a no:"))
for i in range(1,n+1):
    print()
    for j in range(1,n+1):
        if j==i:
            print(i,end="")
        else:
            print("-",end="")