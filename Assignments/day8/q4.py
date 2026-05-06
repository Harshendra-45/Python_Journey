'''
4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. 
If score is at least 70, unlock certificate; otherwise allow retry. 
If progress is less than 80, ask to complete course. 
If subscription is basic, then check progress. 
If progress is at least 50, allow limited access; otherwise lock content. 
If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
'''
Sub = input("enter subscription type: ").lower()
pr = int(input("enter progress: "))
t_score =int(input("enter test score: "))
if Sub=="premium":
    if pr>=80:
        if t_score>=70:
            print("Access Status = Unlock Certificate")
        else:
            print("Access Status = Retry Test")
    else:
        print("Complete full course")
elif Sub=="basic":
    if pr>=50:
        print("Access Status = limited access")
    else:
        print("Access Status = Locked content")
else:
    print("Access Status = Denied")
               
        
       