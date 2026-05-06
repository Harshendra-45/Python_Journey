'''
2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4

'''
n,m = map(int,input("Enter two no's: ").split())
count = 0
'''
if n%7==0:
    for i in range(n,m,7):
        count+=1
else:
    for i in range(n,m):
        if i%7==0:
            count+=1
'''
#for loop 
# for i in range(n,m):
#     if i%7==0:
#         count+=1

#while loop 
# while n<m:
#     if n%7==0:
#         count+=1
#     n+=1

print("count = ",count)