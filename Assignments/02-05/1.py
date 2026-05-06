# 1.Digit Product Analyzer System

# A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

# For every entered number, the system analyzes relationships between its digits.

# Write a program to:

# Find the product of every pair of adjacent digits
# Display all the products
# Find the sum of all these products
# Find the smallest product value
# If the sum of products is divisible by the total number of digits, print Stable Number
# Otherwise print Unstable Number

# Use loops wherever required.

# Input:
# 57294

# Output:
# Products: 35 14 18 36
# Sum = 103
# Smallest = 14
# Unstable Number

n=int(input("enter number "))

sum=0
a=""
s=""
sml="x"
for i in str(n):
    b=int(i)
    if a!="":
        pro=a*b
        sum+=pro
        s=s+" "+str(pro)
        if sml=="x":
            sml=pro
            sml=int(sml)
        else:
            if pro<=sml:
                sml=pro
    a=b
print("products:",s," ")
print("sum = ",sum)
print("smallest = ",sml)
if sum%len(str(sum))==0:
    print("stable number")
else:
    print("unstable number")