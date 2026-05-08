# 1. Adjacent Digit Difference Analyzer

# A system analyzes differences between consecutive digits in a number.

# Write a program to:

# Find the difference between every pair of adjacent digits
# Display all differences
# Count how many differences are even
# Find the largest difference
# If all differences are same → print Uniform Difference
# Else → print Non-Uniform Pattern

# Input:
# 84261

# Output:
# Differences: 4 2 4 5
# Even Differences Count = 3
# Max Difference = 5
# Non-Uniform Pattern

n=int(input("enter number "))

diff=""
dif=0
a=None
count=0
cnt=0
l=len(str(n))
max=0
for i in str(n):
    if a==None:
        a=int(i)
    else:
        b=int(i)
        dif=abs(b-a)
        if dif>=max:
            max=dif
            cnt+=1
        else:
            cnt-=1
        diff+=" "+str(dif)
        if dif%2==0:
            count+=1
        a=b
print("differences: ",diff)
print("Even Differences Count =",count)
print("Max Difference =",max)
if cnt==(l-1):
    print("uniform difference")
else:
    print("non uniform pattern")