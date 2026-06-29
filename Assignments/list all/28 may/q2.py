'''
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
'''
n = int(input("Enter no of students: "))
salary = list(map(int,input("Enter salary: ").split(maxsplit=n)))
sum = 0
for i in salary:
    sum+=i
avg = sum/n
print(avg)
for i in salary:
    if i>avg:
        print(i)
for i in salary[:]:    
    if i<15000:
            # print("yes")
            salary.remove(i)

print(salary)