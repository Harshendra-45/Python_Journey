'''
1
10
1 1
1  0
10101
'''  
n = int(input("Enter a num: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2!=0:
            if i==n:
                print(1,end="") if j%2!=0 else print(0,end="")
            elif j==1:
                print(1,end="")
            elif j==i:
                print(1,end="")
            
            else:
                print(" ",end="")
            
        elif i%2==0:
            if j==1:
                print(1,end="")
            elif j==i:
                print(0,end="")
            else:
                print(" ",end="")
    print()


'''
# Easier way to do it
n = int(input("Enter a num: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):

        if i == n:
            print(1 if j % 2 != 0 else 0, end="")

        elif j == 1:
            print(1, end="")

        elif j == i:
            print(0 if i % 2 == 0 else 1, end="")

        else:
            print(" ", end="")

    print()
'''