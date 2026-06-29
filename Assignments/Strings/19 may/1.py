'''
1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012'''
acc_no = input("Enter account no: ")
i =0
while i<len(acc_no):
    if i<len(acc_no)-4:
        print("*",end="")
    else:
        print(acc_no[i],end="")
    i+=1
     