'''
2.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number'''
num = int(input("Enter transaction id : "))
n = num
rev = 0
dif = 0
count = 0
max = 0
while num>0:
    rem = num%10
    rev = rev*10+rem
    num = num//10
print(rev)
while rev>5:
    dig1=rev%10
    rev=rev//10
    dig2=rev%10
    print("Step Differences:" ,abs(dig1-dig2),end=" ")
    dif +=abs(dig1-dig2)
    if dig1>dig2:
        max = dig1
    else:   
        max=dig2    
print(dif)
count = len(str(n))
if dif%count==0:
    print("Balanced number")
else:
    print("Unbalanced number")