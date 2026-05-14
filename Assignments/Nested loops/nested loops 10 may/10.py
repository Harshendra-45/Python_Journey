'''
enter number6
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
'''
n = int(input("enter a no: "))
i = 1
while i<=n-1:
    print()
    j = 0
    while j<i:
        print(j,end=" ")
        j+=1
    i+=1