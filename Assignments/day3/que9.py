'''
Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500

'''
import math 
dis,mil,price = map(int, input("Enter distance,mileage and petrol price :").split())
print((F'Cost = {((dis/mil)*price):.2f}'))
