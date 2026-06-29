'''
123456789
 1234567
  12345
   123
    1
'''
n = int(input("Enter a no: "))

for i in range(1,n+1):
    p =2*n-2*i+1
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,p+1):
        print(j,end="")
    print()