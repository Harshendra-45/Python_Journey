'''
12345
 1234
  123
   12
    1
'''
n = int(input("Enter a num: "))
for num in range(1,n+1):
    print(num,end="")

for i in range(1,n):
    print()
    for j in range(0,i):
        print(" ",end="")
    for k in range(1,n+1-i):
        print(k,end="")

'''
#Better approach
n = int(input("Enter a num: "))

for i in range(n):

    for j in range(i):
        print(" ", end="")

    for k in range(1, n - i + 1):
        print(k, end="")

    print()
'''