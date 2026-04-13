'''
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2
Output:
Amount = 1210.0
Compound Interest = 210.0
'''

p,r,t = map(int,input("Enter principal,rate & time :").split())
Ci =  (p*(1+r/100)**t)
print(f"Amount = {Ci:.2f}\nCompound Interest = {Ci-p:.2f} ")
