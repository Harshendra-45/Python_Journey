'''
8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500'''
unit1 = int(input("Enter units: "))
unit2 = int(input("Enter units: "))
unit3 = int(input("Enter units: "))
unit4 = int(input("Enter units: "))
unit5 = int(input("Enter units: "))
unit6 = int(input("Enter units: "))
if unit1>unit2:
    if unit1>unit3:
        if unit1>unit4:
            if unit1>5:
                if unit1>6:
                    print(F"Highest stock = {unit1}")
                else:
                    print(F"Highest stock = {unit6}")
            else:
                print(F"Highest stock = {unit5}")
        else:
            print(F"Highest stock = {unit4}")
    else:
        print(F"Highest stock = {unit3}")
else:
    if unit2>unit3:
        if unit2>4:
            if unit2>5:
                if unit2>6:
                    print(F"Highest stock = {unit2}")
                else:
                    print(F"Highest stock = {unit6}")
            else:
                print(F"Highest stock = {unit5}")