'''
6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000
'''
sal = int(input("enter salary: "))
exp = int(input("enter experience: "))
if exp<2:
    print("No Bonus")
elif 2<exp<5:
    print(f"Bonus Amount = {0.05*sal}")
elif 5<exp<10:
    print(f"Bonus Amount = {0.10*sal}")
else:
    print(f"Bonus Amount = {0.20*sal}")