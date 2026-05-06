# 3. Employee Bonus Distribution System
# A company provides bonuses based on years of experience.
# Experience >10 years → 30% bonus
# Experience >5 years → 20% bonus
# Otherwise → 10% bonus
# Write a program to calculate the total salary after adding bonus using inline if.

exp=int(input("enter experience "))
sal=int(input("enter salary "))

bns=30 if exp>10 else 20 if exp>5 else 10
sal=sal+((sal*bns)/100)
print(sal)