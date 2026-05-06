'''
7. A company calculates employee bonuses based on experience,
 performance rating, and salary. The system should take experience (in years), rating, and salary as input. 
If the experience is greater than or equal to 5, then check the rating. If the rating is greater than or equal to 4, then check the salary.
 If the salary is less than 50000, assign a 20% bonus; otherwise, assign a 10% bonus. If the rating is less than 4, assign a 5% bonus.
 If the experience is less than 5, no bonus is given. Display the bonus amount.

Input:
Experience = 6
Rating = 4
Salary = 40000

Output:
Bonus = 8000

'''
exp = int(input("Enter your experience: "))
rating= int(input("Enter your rating: "))
salary = int(input("Enter your salary: "))
if exp>=5:
    if rating>=4:
        if salary<=50000:
            print(F"Bonus = {(20/100)*salary}")
        else:
            print(F"Bonus = {(10/100)*salary}")
    else:
        print(F"Bonus = {(5/100)*salary}")
else:
    print(F"No Bonus")