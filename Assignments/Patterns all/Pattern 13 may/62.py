'''
    1
   123
  12345
 1234567
123456789
'''
n = int(input("Enter a no: "))
for i in range(1,n+1):
    p = i*2-1
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,p+1):
        print(k,end="")
    print()