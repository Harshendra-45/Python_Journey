'''
Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime
'''
import math
n = int(input("enter a number: "))
sum = 0
res = 0
while n>0:
    dig1 = n%10
    n = n//100
    sum = sum + dig1
print("Alternate Sum = ",sum)
for i in range(2,int(math.sqrt(sum)+1)):
    if sum%i == 0:
        res = "Not prime"
        break
else:
    res = "prime"
print(res)