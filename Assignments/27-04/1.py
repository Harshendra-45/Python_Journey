'''
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15
'''
n = int(input("Enter a no: "))
mul = 1
i = 0
#For loop
# for i in range(1,n+1): # range(1,n+1,2) this could be better
#     if i%2!=0:
#         mul *= i

#while loop
while i<n+1:
    # same here i+=2 can generate odd directly
    if i%2!=0: 
        mul*=i
    i+=1


print(mul)