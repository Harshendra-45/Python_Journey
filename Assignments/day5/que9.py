# 9. Library Access System
#    A library checks:

# * If membership is active → Entry allowed
# * If books issued < 3 → Can issue more books

# Input:
# Membership active (yes/no): yes
# Books issued: 2

# Output:
# Entry allowed
# Can issue more books
mem =input("Membership active (yes/no): ").lower()
books = int(input("enter books issued: "))
if mem=="yes":
    print("Entry allowed")
if books<3 and mem=="yes":
    print("can issue more books")