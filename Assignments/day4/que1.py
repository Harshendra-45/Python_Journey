'''
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75
'''

bill,gst,charge,friends = map(int,input("Enter bill amount : ").split())

print(f"Final Bill = {bill + ((gst/100)*bill) + ((charge/100)*bill)}\nEach Person Pays = {(bill + ((gst/100)*bill) + ((charge/100)*bill))/friends}")
