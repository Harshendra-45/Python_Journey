'''
Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
----------------------------------------------------------------
'''

Amount = int(input("enter amount :"))
dis =  0.10*Amount
print(f'Discount = {dis}\nFinal = {Amount-dis}')
