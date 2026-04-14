'''
Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
'''
m1,m2,m3,m4,m5 = map(int,input("Enter marks : ").split())
total = m1+m2+m3+m4+m5
print(f"Total = {total}\nAverage = {total/5}\nPercentage = {(total/500)*100}")

