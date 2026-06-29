'''
*********
 ******* 
  ***** 
   ***
    * 
'''
n = int(input("Enter a no: "))

for i in range(1,n+1):
    
    for k in range(1,i):
        print(" ",end="")
    for j in range(2*n,i*2-1,-1):
        print("*",end="")
    print()