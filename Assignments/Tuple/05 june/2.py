'''QUESTION 2: STUDENT RESULT PROCESSING
=====================================
A training institute wants to manage student records using NamedTuple.
Fields:
roll_no, name, course, marks
Requirements:
1. Read N student records from the user and store them in a list of NamedTuples.
---
2. Display all student details.
---
3. Find and display the topper of the class.
---
4. Count and display the number of students scoring above 80 marks.
---
5. Calculate and display the average marks.
---
6. Accept a course name from the user and display all students enrolled in that course.
---
Test Case:
Input:
Enter number of students: 4
1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88
Enter course: Python
Expected Output:
Topper:
3 Karan Python 92
Students Above 80:
3
Average Marks:
85.75
Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
'''
from collections import namedtuple
student = namedtuple("student",["rollno","name","course","marks"])
n = int(input("Enter a no:"))
st_list = []
for i in range(n):
    id = int(input("Enter id: "))
    name = (input("Enter name: "))
    dep = input("Enter course name: ")
    sal = float(input("Enter marks: "))
    st_list.append(student(id,name,dep,sal))

print(st_list)
max= st_list[0]
for s in st_list:
    if s.marks>max.marks:
        max=s
print("Topper",max)
co = 0
for s in st_list:
    if s.marks>80:
        co+=1
print("Students above 80 = ",co)
sums = 0
for m in st_list:
    sums+=m.marks
print("Average",sums/n)
crs = input("enter course name to display: ")
for cr in st_list:
    if cr.course==crs:
        print(cr)