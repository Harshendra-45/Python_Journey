'''
Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0
'''

price,dp,rate,dur = map(int,input("Enter all values :").split())
rem = price - dp
inter = (rate/100)*rem
total = rem  + inter
print(F"Remaining Amount = {price - dp}\nTotal with Interest = {total}\nMonthly EMI = {total/dur}")
