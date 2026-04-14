'''
Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0

---
'''
pr,rate,time = map(int,input("Enter principal,rate & time : ").split())
Ci =  (pr*(1+rate/100)**time)
print(F"Amount after interest = {Ci}")
