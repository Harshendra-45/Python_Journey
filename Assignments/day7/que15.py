'''
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''
veh = input("Enter vehicle type: ").lower()
hrs = int(input("Enter hrs parked: "))
if veh =="bike":
    if hrs<5:
        print(F'Total Parking Fee: ₹{(10*hrs)}')
    else:
        print(F'Total Parking Fee: ₹{(10*hrs)+100}')
elif veh =="car":
    if hrs<5:
        print(F'Total Parking Fee: ₹{(20*hrs)}')
    else:
        print(F'Total Parking Fee: ₹{(20*hrs)+100}')
else:
    if hrs<5:
        print(F'Total Parking Fee: ₹{(50*hrs)}')
    else:
        print(F'Total Parking Fee: ₹{(50*hrs)+100}')

