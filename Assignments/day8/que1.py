'''1. Insurance Claim Approval System

An insurance company processes claims based on policy age, claim amount, and accident type. 
The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. 
If the claim amount is up to 50000, then check the accident type.
If it is minor, approve the claim; otherwise, approve it with inspection.
If the claim amount is between 50001 and 200000, then check the accident type. 
If it is major, approve with investigation; otherwise reject. 
If the claim amount exceeds 200000, reject. 
If the policy age is less than 2 years, then check accident type. 
If minor, reject; otherwise mark as pending review.


Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major

Output:
Claim Status = Approved with Investigation
'''
policy_age = int(input("Enter policy age: "))
cl_amount = int(input("Claim amount: "))
ac_type = input("Accident Type: ").lower()
if policy_age>2:
    if cl_amount<=50000:
        if ac_type =="minor":
            print("Claim Status = Approved ")
        else:
            print("Claim Status = Approved with Inspection")
    elif 50001<cl_amount<200000:
        if ac_type=="major":
            print("Claim Status = Approved with Investigation")
        else:
            print("Claim Status = Rejected")
else:
    if ac_type=="minor":
        print("Claim Status = Rejected")
    else:
        print("Claim Status = Marked For Review")