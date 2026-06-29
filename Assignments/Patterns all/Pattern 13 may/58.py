'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
'''
n = int(input("Enter a num: "))
i = 1
while i<=n:
    j = 1
    while j<=n-i:
        print(" ",end="")
        j+=1
    k = 1
    while k<=i:
        print(k,end=" ")
        k+=1
    i+=1
    print()