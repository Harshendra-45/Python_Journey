# 5. Banking Security System
#    A bank validates login attempt:

# * If username is "admin" → Valid user
# * If password length ≥ 8 → Strong password

# Input:
# Enter username: admin
# Enter password: secure123

# Output:
# Valid user
# Strong password
username = input("Enter username : ")
pwd = input("enter password: ")
if username =="admin":
    print("Valid user")
if len(pwd)>=8:
    print("Strong password")