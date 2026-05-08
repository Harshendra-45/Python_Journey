# 4.Digit Gap Consistency Checker

# A number analysis system checks whether the gap between digits follows a consistent pattern.

# Write a program to:

# Find the absolute difference between first two digits
# Compare this difference with all next adjacent digit differences
# If any difference is not equal to the first difference, stop using break
# Display:
# - Initial gap
# - Whether all gaps are same or not

# Input:
# 8642

# Output:
# Initial Gap = 2
# Consistent Pattern

# Input:
# 97531

# Output:
# Initial Gap = 2          # -2 
# Consistent Pattern

# Input:
# 5321

# Output:
# Initial Gap = 2
# Pattern Break Detected

n=int(input("enter the number "))

a=None
b=None
d=0
x=True
for i in str(n):
    if a==None:
        a=int(i)
    elif b==None:
        b=int(i)
        d=(b-a)
        print("initial gap = ",d)
        a=b
    else:
        b=int(i)
        if (b-a)==d:
            a=b
        else:
            print("break pattern detected")
            x=False
            break
if x==True:
    print("consistent pattern")
    
    

        