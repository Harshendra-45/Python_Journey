n = int(input("Enter a num: "))
i = 1
while i<=n:
    print()
    j = 1
    while j<=i:
        if j%2==0:
            print("*", end=" ")
        else:
            print(j, end=" ")
        j+=1
    i+=1