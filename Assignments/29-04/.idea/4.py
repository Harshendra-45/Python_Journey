'''
Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code
'''
n = int(input("Enter a number: "))
b = n
for i in range(1,len(str(b))):
    dig = n % 10
    n = n // 10
    if str(dig) in str(n):
            print("Rejected")
            break
else:
        print("Valid Unique Code")
