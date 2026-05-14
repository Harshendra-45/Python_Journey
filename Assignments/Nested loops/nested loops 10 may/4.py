'''
1
00
111
0000
11111
'''
n = int(input("Enter a num: "))
# i = 1
# while i<=n:
#     print()
#     j = 1
#     while j<=i:
#         if i%2==0:
#             print(0,end="")
#         else:
#             print(1,end="")
#         j+=1
#     i+=1

for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        if i%2==0:
            print(0,end="")
        else:
            print(1,end="")
            