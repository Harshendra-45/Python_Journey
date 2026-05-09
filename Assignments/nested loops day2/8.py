'''
enter n6
 654321
  65432
   6543
    654
     65
'''
n = int(input("Enter a num: "))
i = 1
while i<=n-1:
    print()
    c = 1
    while c<=i-1:
         print(" ",end="")
         c+=1
    j = n
    while j>=i:
        print(j,end="")
        j-=1
    i+=1