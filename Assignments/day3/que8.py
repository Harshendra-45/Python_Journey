'''
Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0
----------------------------------------------------------------------
'''

Mb = int(input("enter Mb :"))
print(f"GB = {Mb/1024}")
