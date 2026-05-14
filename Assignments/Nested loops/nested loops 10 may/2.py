'''
WAP to print Square, Cube and Square Root of all numbers from 1 to N'''
n = int(input("enter a no: "))
# i = 1
# while i<=n:
#     print(f"Square of {i} = {i**2}")
#     print(f"cube of {i} = {i**3}")
#     print(f"Square root of {i} = {i**0.5}")
#     i+=1
import math
for i in range(1,n+1):
        print(F"square = {i**2},cube={i**3},square root ={math.sqrt(i)}")