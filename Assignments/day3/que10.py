'''
Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
'''

total,obtained = map(int,input("enter total & obtained marks : ").split())
print(f'Percentage = {(total/obtained)*100} ')

