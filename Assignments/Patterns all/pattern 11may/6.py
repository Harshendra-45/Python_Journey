'''
6) Number Triangle with Dashes
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9
'''
n = int(input("Enter a num: "))

for i in range(1,n+1):
    print()
    k = i
    for j in range(1,n-i+1):
        print("-",end="")
    for l in range(1,i+1):
        print(k,end="")
        k+=1    