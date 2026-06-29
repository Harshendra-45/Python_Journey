''' 2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.
'''
python = set()
java = set()
while True:
    print(" Menu:\n\
    1. Enroll Student in Python\n\
    2. Enroll Student in Java\n\
    3. Display Python Students\n\
    4. Display Java Students\n\
    5. Find Students Enrolled in Both Courses\n\
    6. Find Students Enrolled Only in Python\n\
    7. Find Students Enrolled Only in Java\n\
    8. Check Enrollment in Python Course\n\
    9. Display Total Unique Students\n\
    10. Exit")

    ch = int(input("Enter a choice: "))
    match ch:
        case 1:
            python.add(input("Enter name: "))
        case 2:
            java.add(input("Enter name: "))
        case 3:
            print("Students in python club are\n",python)
        case 4:
            print("Students in java club are\n",java)
        case 5:
            print("Students in both club:\n",python.intersection(java))
        case 6:
            print("students only in python club\n",python.difference(java))
        case 7:
            print("students only in java club\n",java.difference(python))
        case 8:
            inter = input("Enter name: ")
            print("Enrollment in python course\n",inter in python)
        case 9:
            print("Total uniques members:\n",len(python|java))
        case 10:
            print("Exiting ...")
            break
        case _:
            print("Invalid choice")