'''====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
'''
from collections import namedtuple
Employee = namedtuple("Employee",["emp_id","emp_name","department","salary"])
n = int(input("Enter a no:"))
emp_list = []
for i in range(n):
    id = int(input("Enter id: "))
    name = (input("Enter name: "))
    dep = input("Enter department name: ")
    sal = float(input("Enter salary: "))
    emp_list.append(Employee(id,name,dep,sal))

print(emp_list)

max= emp_list[0]
min=emp_list[0]
for s in emp_list:
    print(s.salary)
    if s.salary>max.salary:
        max=s
print(max)

for m in emp_list:
    if m.salary<min:
        min=m 
print("min",min)
sums = 0
for i in emp_list:
    sums+=i.salary
print("Average",sums/n)
depname = input("Enter employee department to display: ")
print("Details")
for i in emp_list:
    if depname==i.department:
        print(i)
