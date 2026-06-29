'''
55555
 4__4
  3_3
   22
    1

'''
n = int(input("Enter a num: "))
for num in range(1,n+1):
        print(n,end="")
print()
for i in range(1,n):
    for j in range(1,i+1):
        print(" ", end="")

    for k in range(1, n - i + 1):
        if k==1 or k==n-i:
            print(n-i, end="")
        else:
             print("_",end="")

    print()