'''
Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
''' 

hrs,min,sec = map(int,input("enter hours,minutes & seconds: ").split())
print(f"Total Seconds = {(hrs*3600)+(min*60)+(sec)}")
