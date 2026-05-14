'''
2.
Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496'''

n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))
print("Perfect number are: ")
while n<m:
    i = 1
    sum = 0
    while i<=n//2:
        if n%i==0:
            sum+=i
        i+=1
    if sum==n:
        print(n)
    n+=1
