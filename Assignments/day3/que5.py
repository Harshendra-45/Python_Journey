'''
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
------------------------------------------------------------
'''

mark1 , mark2, mark3 = map(int, input("enter three marks : ").split())
print(f'Average : {(mark1+mark2+mark3)/3}')
