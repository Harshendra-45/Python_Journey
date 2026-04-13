'''
Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output: Average Speed = 50 km/h
'''
d1,t1,d2,t2 = map(int,input("Enter distance and time for both trips : ").split())
print(F"Average Speed = {((d1*t1)+(d2*t2))/(t1*t2)}")
