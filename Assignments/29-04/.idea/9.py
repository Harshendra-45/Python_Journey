'''
Bike Service Kilometer Checker

A bike needs service every 3000 km.

Write a program to:

- Read travelled kilometers
- Print every service checkpoint till entered km

Input:
10000

Output:
3000 6000 9000
'''
km = int(input("Enter the travelled kilometers: "))
for i in range(0,km,3000):
    if i==0:
        continue
    else:
        print(i,end=" ")