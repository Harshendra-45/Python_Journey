# 2.
# Digit Order Break Analyzer

# A number validation system checks whether digits of an ID follow a strict increasing pattern. The moment the pattern breaks, the system stops further checking.

# Write a program to:

# Traverse the digits from left to right
# Check whether each digit is greater than the previous digit
# If the pattern breaks at any point, stop checking further using break
# Display the position where the order breaks (1-based index)
# If no break occurs, print Strictly Increasing Number

# Use loops and break wherever required.

# Input:
# 12357

# Output:
# Strictly Increasing Number

# Input:
# 12342

# Output:
# Break at position = 4
# # Not Increasing Number


n=int(input("enter the number "))

a=None
b=0
x=True
for i in str(n):
    if a==None:
        a=int(i)
    else:
        b=int(i)
        if a>b:
            print("break at position = ",a)
            print("not increasing number")
            x=False
            break
        else:
            a=b
if x==True:
    print("strictly increasing order")

            