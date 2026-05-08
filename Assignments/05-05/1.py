 #1. Smart Shopping Mall Discount System
# A shopping mall offers discounts based on customer type and purchase amount.
# If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
# If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
# Write a program to calculate the final payable amount using inline if only.

cstm=input("customer type (premium/regular): ")
amt=int(input("enter the purchased amount "))

dis=20 if cstm=="premium" and amt>5000 else 10 if cstm=="premium" else 10 if amt>3000 else 5
pay = amt-((amt*dis)/100)
print("payable amount =",pay)