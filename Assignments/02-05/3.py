# 3. Zero Detection & Early Termination System

# A financial system scans transaction IDs digit by digit.
# If a digit '0' is found, the system immediately stops processing further digits for security reasons.

# Write a program to:

# Traverse each digit of the number from right to left
# Display each digit processed before encountering 0
# Stop the loop immediately when 0 is found using break
# Count how many digits were processed before termination
# If no zero is found, print No Zero Found

# Use loops and break wherever required.

# Input:
# 572049

# Output:
# Digits Processed: 9 4
# Count = 2
# Zero Found - Process Stopped

# Input:
# 56789

# Output:
# Digits Processed: 9 8 7 6 5
# Count = 5
# No Zero Found

n=int(input("enter the number "))

count=0
d=""
x=True
while n>0:
    if n%10==0:
        x=False
        break
    else:
        count+=1
        d=d+" "+str(n%10)
        n=n//10
print("digits processed : ",d)
print("count = ",count)
if x==True:
    print("no zero found")
else:
    print("zero found - process stopped")
        