'''
Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
'''

n100,n50,n10 = map(int,input("Enter 100,50,10 notes count: ").split())
print(f"Amount = {(n100*100)+(n50*50)+(n10*10)}")
