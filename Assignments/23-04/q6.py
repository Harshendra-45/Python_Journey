'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. 
A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong'''
n=int(input("Enter a num: "))
b=n
sum = 0
while n>0:
    num = n%10
    sum += num**3
    n = n//10
if b==sum:
    print("Armstrong")
print("Done")