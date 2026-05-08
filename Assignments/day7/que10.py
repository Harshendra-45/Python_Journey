'''
10. Mobile Data Plan Advisor


A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan

'''
dausa= float(input("Enter daily data usage: "))
if dausa<1:
    print("Recommended Plan: Basic Plan")
elif 1<dausa<3:
    print("Recommended Plan: Standard Plan")
else:
    print("Recommended Plan: Premium Plan")