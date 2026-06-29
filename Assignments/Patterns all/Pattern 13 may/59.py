'''
    A
   A B
  A B C
 A B C D
A B C D E  
'''
n = int(input("Enter a num: "))
# i = 1
# while i<=n:
#     j = 1
#     while j<=n-i:
#         print(" ",end="")
#         j+=1
#     ch = 65
#     k=1
#     while k<=i:
#         print(chr(ch),end=" ")
#         ch+=1
#         k+=1
#     i+=1
#     print()

for i in range(1,n+1):
    ch=65
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()