
'''.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number
'''
n = int(input("enter a num: "))
z = 0
for i in str(n):

    if z>=int(i):
        print("unstable Number")
        break
    else:
        z = int(i)
else:
    print("stable Number")