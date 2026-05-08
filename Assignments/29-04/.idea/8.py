'''
ATM Note Counter

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7
'''
amt = int(input("Enter amount:"))
notes = 0
for i in range(amt):
    if i*100==amt:
        notes = i
        break
print(notes)