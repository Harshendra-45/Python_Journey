'''
1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers.
To identify password strength, the system finds the highest digit present in the entered password. 
Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9'''
n = int(input("Enter a num: "))
num = 0
while n>0:
    d = n%10
    if d>num:
        num = d
    n = n//10
    
print("biggest num is", num)