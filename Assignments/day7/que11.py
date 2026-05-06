'''
11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600
'''
dis = int(input("Enter distance: "))
clas = input("Enter class: ").lower()
if dis<=100:
    if clas =="sleeper":
        print("Total Fare: ₹100")
    else:
        print("Total Fare: ₹200")
elif 100<dis<500:
    if clas =="sleeper":
        print("Total Fare: ₹300")
    else:
        print("Total Fare: ₹600")
else:
    if clas =="sleeper":
        print("Total Fare: ₹500")
    else:
        print("Total Fare: ₹1000")