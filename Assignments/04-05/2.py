# 2. Digit Sum Mirror Checker

# A validation system checks symmetry in digit sums.

# Write a program to:

# Split number into two halves
# Find sum of first half digits
# Find sum of second half digits
# Display both sums
# If both sums are equal → print Balanced Number
# Else → print Unbalanced Number

# Input:
# 123321

# Output:
# First Half Sum = 6
# Second Half Sum = 6
# Balanced Number

n=int(input("enter the number "))

sum1=0
sum2=0
l=len(str(n))
count=1

if l%2==0:
    for i in str(n):
        if count<=l/2:
            sum1+=int(i)
            count+=1
        else:
            sum2+=int(i)
print("first half sum = ",sum1)
print("second half sum = ",sum2)
if sum1==sum2:
    print("balanced number")
else:
    print("unbalanced number")