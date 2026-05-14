'''
1
01
101
0101
10101
'''
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2!=0:
            if j%2!=0:
                print(1,end="")
            else:
                print(0,end="")
        elif i%2==0:
            if j%2==0:
                print(1,end="")
            else:
                print(0,end="")
        
    print()


# n = int(input("Enter a num: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print((i + j) % 2, end="")
#     print()