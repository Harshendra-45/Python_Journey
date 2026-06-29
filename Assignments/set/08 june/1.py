'''1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.'''

coding_club =set()
robo_club =set()
while True:
    print(" Menu:\
    1. Add Student to Coding Club\
    2. Add Student to Robotics Club\
    3. Display Students in Coding Club\
    4. Display Students in Robotics Club\
    5. Find Students in Both Clubs\
    6. Find Students Only in Coding Club\
    7. Find Students Only in Robotics Club\
    8. Display All Unique Club Members\
    9. Display Total Unique Club Members\
    10. Exit")
    ch = int(input("Enter a choice: "))
    match ch:
        case 1:
            coding_club.add(input("Enter ids: "))
        case 2:
            robo_club.add(input("Enter ids: "))
        case 3:
            print("Students in coding club are\n",coding_club)
        case 4:
            print("Students in robotics club are\n",robo_club)
        case 5:
            print("Students in both club:\n",coding_club.intersection(robo_club))
        case 6:
            print("students only in coding club\n",coding_club.difference(robo_club))
        case 7:
            print("students only in robotics club\n",robo_club.difference(coding_club))
        case 8:
            print("Uniques club members\n",robo_club|coding_club)
        case 9:
            print("Total uniques members:\n",len(robo_club|coding_club))
        case 10:
            print("Exiting ...")
            break
        case _:
            print("Invalid choice")