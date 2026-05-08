'''
5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops*.

Input: 121
Output: Palindrome'''
n = int(input("enter a no: "))
for i in str(n):
    dig = n%10
    if i==str(dig):
        n = n//10 
    print("palindrome")  