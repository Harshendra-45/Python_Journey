'''
5 5 5 5 5
 4 4 4 4
  3 3 3 
   2 2
    1
'''
n = int(input("Enter a no: "))
b=n
for i in range(1,n+1):
    
    for k in range(1,i):
        print(" ",end="")
    for j in range(n,i-1,-1):
        print(b,end=" ")
    b-=1   
    print()