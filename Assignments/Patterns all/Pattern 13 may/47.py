'''
    1
   11
  1*1
 1**1
11111
'''
n = int(input("Enter a num: "))
i = 1
while i<=n-1:
    j = 1
    while j<=n-i:
        print(" ",end="")
        j+=1
    k = 1
    while k<=i:
        if k==1 or k==i:
            print(1,end="")
        else:
            print("*",end="")
        k+=1
    i+=1
    print()
for i in range(1,n+1):
    print(1,end="")
    

'''
n = int(input("Enter a num: "))

i = 1

while i <= n:

    j = 1

    while j <= n - i:
        print(" ", end="")
        j += 1

    k = 1

    while k <= i:

        if i == n:
            print(1, end="")

        elif k == 1 or k == i:
            print(1, end="")

        else:
            print("*", end="")

        k += 1

    print()
    i += 1
'''