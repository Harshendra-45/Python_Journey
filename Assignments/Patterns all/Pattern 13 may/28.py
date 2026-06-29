'''
1
123
12345
1234567
123456789
'''
n = int(input("Enter a num: "))
for i in range(1,n+1):
    k = 1
    for j in range(0,i*2-1):
        print(k,end="")
        k+=1
    print()