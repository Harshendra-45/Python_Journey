'''
Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0

---
'''

data = int(input("enter value : "))
print(f"In MB = {data*1024}\nIn KB = {data*1048576}")
