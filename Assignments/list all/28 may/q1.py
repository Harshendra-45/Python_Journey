'''
1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3
'''
n = int(input("Enter no of students: "))
student = list(map(int,input("Enter marks: ").split(maxsplit=n)))
print(student)
max=student[0]
min = student[0]
count=0
for i in student:
    if max<i:
        max=i
    elif min>i:
        min=i
    if i>75:
        count+=1
print("max",max)
print("min",min)
print("count",count)