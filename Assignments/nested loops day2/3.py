'''
WAP to find out all the leap years between two entered years
'''
n = int(input("Enter a no:"))
m = int(input("Enter a no:"))
# while n<=m:
#     if n%100==0:
#         if n%400==0:
           
#          print(n)
#     else:
#         if n%4==0:
#             print(n)
#     n+=1
for i in range(n,m+1):
    if i%4==0 and i%100!=0 or i%400==0:
        print(i)