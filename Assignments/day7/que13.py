'''
13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600
'''
sal = int(input("Enter salary: "))
rat = int(input("Enter rating: "))
if rat==1:
    print("No hike")
elif rat==2:
    print(f"Revised Salary: {(0.05*sal)+sal}")
elif rat==3:
    print(f"Revised Salary: {(0.10*sal)+sal}")
elif rat==4:
    if sal<20000:
        print(f"Revised Salary: {(0.20*sal)+sal+2000}")
    else:
        print(f"Revised Salary: {(0.20*sal)+sal}")
else:
    if sal<20000:
        print(f"Revised Salary: {(0.25*sal)+sal+2000}")
    else:
        print(f"Revised Salary: {(0.25*sal)+sal}")
