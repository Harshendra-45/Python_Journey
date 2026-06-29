'''
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID'''
emp = input("Enter string: ")
valid=0
if len(emp)==8:
    if emp[:3]=="EMP" and emp[3:].isdigit():
        valid=1
else:
    print("Invalid")
print("Valid emp id ")if valid==1 else print("Invalid")