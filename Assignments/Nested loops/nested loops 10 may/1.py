'''
WAP to find out the sum of all integer between 100 and 200 which are divisible by 9
'''
n = int(input("enter a no:"))
m = int(input("enter a no:"))
sum = 0
# while n<=m:
#     if (n%9==0):
#         sum+=n
#     n+=1
# print(sum)

for i in range(n,m+1):
    if i%9==0:
        sum+=i
print(sum)