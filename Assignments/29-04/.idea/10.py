'''
Lift Mode Operation – Advanced Smart Elevator System

A smart building elevator works in multiple intelligent modes based on the mode number entered by the control panel.
The system must automatically execute floor movement instructions using loops.

Write a program:

- If mode = 1
  Normal Up Mode activated.
  Read current floor and destination floor.
  Print all floors from current to destination in ascending order.

- Else if mode = 2
  Down Mode activated.
  Read current floor and destination floor.
  Print all floors from current to destination in descending order.

- Else if mode = 3
  Energy Saving Mode activated.
  Read destination floor.
  Lift starts from ground floor (0) and stops only on alternate floors till destination.

- Else
  Emergency Mode activated.
  Print "Emergency Alarm" 4 times using loop.

Input:
3
6

Output:
0 2 4 6


Input:
1
2
7

Output:
2 3 4 5 6 7


Input:
2
8
3

Output:
8 7 6 5 4 3

Input:
5

Output:
Emergency Alarm
Emergency Alarm
Emergency Alarm
Emergency Alarm
'''
mode = int(input("Enter mode: "))
if mode == 1:
    c =int(input("Enter current floor: "))
    d =int(input("Enter destination floor: "))
    for i in range(c,d+1):
        print(i,end=" ")
elif mode == 2:
    c = int(input("Enter current floor: "))
    d = int(input("Enter destination floor: "))
    for i in range(c, d-1,-1):
        print(i, end=" ")
elif mode == 3:
    d =int(input("Enter destination floor: "))
    for i in range(0,d,2):
        print(i, end=" ")
else:
    for i in range(1,5):
        print("Emergency Alarm")