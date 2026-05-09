'''
enter n = 6
     *
    **
   ***
  ****
 *****
******
'''
n = int(input("Enter a no: "))
i = 1
while i<=n:
    print()
    c = 1 
    while c<=n-i:
            print(" ",end="")
            c+=1
        
    d = 1
    while d<=i:
            print("*",end="")
            d+=1
    i+=1