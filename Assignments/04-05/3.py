# 3. Digit Neighbor Sum Analyzer

# A system analyzes the relationship between a digit and its immediate neighbors.

# Write a program to:

# Traverse digits from left to right (ignore first and last digit)
# For each digit, calculate sum of its adjacent digits
# Check if current digit is equal to the sum of its neighbors
# Display such digits
# Count how many such digits exist
# If none found → print No Matching Digit
# Else → print Neighbor Sum Pattern Found

# Input:
# 121314

# Output:
# Matching Digits: 2 3        #only 2
# Count = 2
# Neighbor Sum Pattern Found

n=int(input("enter the number "))

a=None
b=None
count=0
mch=""
for i in str(n):
    if a==None:
        a=int(i)
    elif b==None:
        b=int(i)
    else:
        c=int(i)
        if (a+c)==b:
            mch+=" "+str(b)
            count+=1
        a=b
        b=c

print("matching digits: ",mch)
print("count = ",count)
if count>0:
    print("Neighbor Sum Pattern Found")
else:
    print("print No Matching Digit")