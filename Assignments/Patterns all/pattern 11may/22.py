'''
22) Inverted Hollow Pyramid
    *********
     *     *
      *   *
       * *
        *
'''
n = int(input("enter a num: "))
for i in range(1,n+1):
    print()
    for j in range(1,n*2):
        if i==1 or i==j or i+j==8:
            print("*",end=" ")
        else:
            print(" ",end="")