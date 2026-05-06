# 4.Digit Gap Analyzer

# A system analyzes the gap between consecutive digits.

# Write a program to:

# Traverse digits from left to right
# Find the absolute difference between current digit and next digit
# Display each difference
# Count how many differences are greater than 2
# Find the maximum difference
# If all differences ≤ 2 → print Smooth Number
# Else → print Irregular Pattern

# Input:
# 86421

# Output:
# Differences: 2 2 2 1
# Count (>2) = 0
# Max Difference = 2
# Smooth Number

n=int(input("enter the number "))

count=0
max=0
diff=""
x=True
a=None
for i in str(n):
    if a==None:
        a=int(i)
    else:
        b=int(i)
        dif=abs(b-a)
        if dif>=max:
            max=dif
        diff=diff+" "+str(dif)
        if dif>2:
            count+=1
            x=False
        a=b
        
print("differences: ",diff)
print("count (>2) = ",count)
print("max difference = ",max)
if x==True:
    print("smooth number")
    