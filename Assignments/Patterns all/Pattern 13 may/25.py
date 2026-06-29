'''
5
54
543
5432
54321
'''
n = int(input("Enter a num: "))
for i in range(1,n+1):
    b=n
    for j in range(1,i+1):
        print(b,end="")
        b-=1
    print()