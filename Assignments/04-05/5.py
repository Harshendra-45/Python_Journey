# 5.Tech Number Checker

# A number is called a Tech Number if:

# It has even number of digits
# Split it into two equal halves
# Add both halves
# Square the sum
# If result equals original number → Tech Number

# Write a program to:

# Count digits
# If digits are even, split the number
# Find sum of both halves
# Square the sum
# Display intermediate values
# Check and print result

# Input:
# 2025

# Output:
# First Half = 20
# Second Half = 25
# Sum = 45
# Square = 2025
# Tech Number

n=int(input("enter the number "))

hlf1=""
hlf2=""
count=1
l=len(str(n))

if l%2==0:
    for i in str(n):
        if count<=l/2:
            hlf1+=i
            count+=1
        else:
            hlf2+=i
print("first half = ",hlf1)
print("second half = ",hlf2)
sum=int(hlf1)+int(hlf2)
print("sum = ",sum)
sqr=sum**2
print("square = ",sqr)
if sqr==n:
    print("tech number")