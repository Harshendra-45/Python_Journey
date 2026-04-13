'''
Assignment 4: Area of Rectangle

Write a Python program that:

Accepts length and breadth.
Calculates area.

Input:
Length = 10
Breadth = 5

Output:
Area = 50
------------------------------------------------
'''

len , brt = map(int, input("enter length and breadth : ").split())
print(F"Area = {len*brt}")
