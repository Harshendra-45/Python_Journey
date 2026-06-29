'''
55555
 4444
  333
   22
    1
'''
n = int(input("Enter a num: "))

for i in range(n):

    for j in range(i):
        print(" ", end="")

    for k in range(1, n - i + 1):
        print(n-i, end="")

    print()