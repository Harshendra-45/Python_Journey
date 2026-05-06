# 5. Digit Alternating Sum System

# A coding system calculates alternating sum of digits (add, subtract, add...).

# Write a program to:

# Traverse digits from left to right
# Add first digit, subtract second, add third, and so on
# Display final alternating sum
# If result is positive → print Positive Pattern
# Else → print Negative Pattern

# Input:
# 1234

# Output:
# Result = -2
# Negative Pattern

# Input:
# 8642

# Output:
# Result = 8                         # result= 4
# Positive Pattern

n=int(input("enter the number "))

sum=0
count=0
for i in str(n):
    count+=1
    if count%2==0:
        sum=sum-int(i)
    else:
        sum+=int(i)
print("result = ",sum)
if sum>=0:
    print("positive pattern")
else:
    print("negative pattern")