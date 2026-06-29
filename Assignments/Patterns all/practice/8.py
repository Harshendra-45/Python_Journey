# n = int(input("Enter a num: "))
# for i in range(1,2*n):
#     for k in range(1,2*n):
#         if i==1 or i==2*n-1 or k==1 or k==2*n-1:
#             print(n,end="")
#         elif i==n-i or i==(2*n)-(n-2) :
#             print(n-1,end="")
#         elif i==n-(n-1) or i==2*n-(n-3) :
#             print(2*n-k,end="")
#         else:
#             print(" ",end="")
#     print()

n = int(input("Enter a num: "))

for i in range(1, 2*n):

    for k in range(1, 2*n):

        # outer layer
        if i == 1 or i == 2*n-1 or k == 1 or k == 2*n-1:
            print(n, end=" ")

        # second layer
        elif i == 2 or i == 2*n-2 or k == 2 or k == 2*n-2:
            print(n-1, end=" ")

        # third layer
        elif i == 3 or i == 2*n-3 or k == 3 or k == 2*n-3:
            print(n-2, end=" ")

        else:
            print(1, end=" ")

    print()