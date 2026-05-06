'''
3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000'''
inc = int(input("enter annual income: "))
if inc<=250000:
    print("No tax")
elif 250000<inc<=500000:
    print(F'Tax Payable = {0.05*inc}')
elif 500001<=inc<=100000:
    print(F'Tax Payable = {0.20*inc}')
else:
    print(F'Tax Payable = {0.30*inc}')

