# 8. Number Property Checker
#    A system evaluates number properties:

# * If number % 2 == 0 → Even number
# * If number % 5 == 0 → Divisible by 5

# Input:
# Enter number: 20

# Output:
# Even number
# Divisible by 5
num = int(input("enter number :"))
if num%2==0:
    print("Even Number")
if num%5==0:
    print("Divisible by 5")