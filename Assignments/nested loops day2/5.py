'''
A
AB
ABC
ABCD
ABCDE
'''
n = int(input("Enter a no: "))
# i = 1
# while i<=n:
#     print()     
#     j = 1
#     chrc = 65
#     while j<=i:
#         print(chr(chrc),end="")
#         j+=1
#         chrc+=1
#     i+=1
'''We can make multiple patterns like these by 
    just changing chrc or some loop setting '''
for i in range(1,n+1):
    