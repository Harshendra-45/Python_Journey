# 7. Salary Benefits System
#    A company provides benefits:

# * If salary ≥ 30000 → Eligible for PF
# * If salary ≥ 50000 → Eligible for bonus

# Input:
# Enter salary: 55000

# Output:
# PF applicable
# Bonus applicable
sal = int(input("enter salary: "))
if sal>=30000:
    print("Eligible for PF")
if sal>=50000:
    print("Eligible for Bonus")