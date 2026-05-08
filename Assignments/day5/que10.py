# 10. Online Exam System
#     System evaluates exam conditions:

# * If marks ≥ 40 → Pass
# * If attendance ≥ 75 → Eligible for certificate

# Input:
# Enter marks: 60
# Enter attendance: 80

# Output:
# Pass
# Eligible for certificate
marks = int(input("enter marks : "))
attendance = int(input("enter attendance : "))
if marks>=40:
    print("pass")
if marks>40 and attendance>=75:
    print("eligible for certificate")
