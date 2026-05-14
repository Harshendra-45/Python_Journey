'''
1) Hollow Pyramid
        *
       * *
      *   *
     *     *
    *********
'''
n = int(input("Enter a num: "))
for i in range(1,n+1):
    if i<n:
        prev = n-i+1
        next = n+i-1
        for j in range(1,n*2):
            if  j==prev or j == next:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,n*2):
            print("*",end="")