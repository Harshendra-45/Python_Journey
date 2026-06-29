'''
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''
n = int(input("Enter a no: "))

for i in range(1,n+1):
    
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        p=k
        if k==1 or k==i:
            print(1,end=" ")
        elif k==i-1:
            print(p,end=" ")
        else:
            print(i-1,end=" ")
        p+=k   
    print()

#error not completed