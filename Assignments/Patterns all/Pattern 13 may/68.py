'''
    #
   *#* 
  **#** 
 ***#*** 
****#****
'''
n = int(input("Enter a no: "))
for i in range(1,n+1):
    p = 2*i-1
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,p+1):
        if k==i:
            print("#",end="")
        else:
            print("*",end="")
    print()
