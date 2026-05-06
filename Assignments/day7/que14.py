'''
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000'''
course = input("Enter course:").lower()
user = input("Enter user type:").lower()
if course == "programming":
    if user =="student":
        print(f"Final course fee:{5000-(0.20*5000)}")
    elif user =="working":
        print(f"Final course fee:{5000-(0.10*5000)}")
    else:
        print(f"Final course fee:{5000}")
elif course == "marketing":
    if user =="student":
        print(f"Final course fee:{3000-(0.20*3000)}")
    elif user =="working":
        print(f"Final course fee:{3000-(0.10*3000)}")
    else:
        print(f"Final course fee:{3000}")
else:
    if user =="student":
        print(f"Final course fee:{4000-(0.20*4000)}")
    elif user =="working":
        print(f"Final course fee:{4000-(0.10*4000)}")
    else:
        print(f"Final course fee:{4000}")