'''
Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5
'''

msalary,wdays,whpd = map(int,input("enter msalary,wdays & whpd :").split())
print(f"Salary per daay = {msalary/wdays}\nSalary per hour = {msalary/(wdays*whpd)}") 
