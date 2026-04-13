'''
Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
----------------------------------------
'''
distance, time = map(int,input("enter distance and  time : ").split())
print(f"Speed = {distance/time} km/h")
