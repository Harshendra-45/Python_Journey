'''
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number'''
num = input("enter vehicle no: ")
valid = 0
if len(num)==10:
    s = num[:2]
    n = num[2:4]
    if s.isalpha() and n.isdigit()==True:
        print("Valid vehicle Number")
    else:
        print("Invalid number")