'''
1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime
'''
import math
n = int(input("Enter a num: "))
b = n
sum = 0
reverse = 0
difference = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
    reverse = reverse*10+digit
difference = abs(b-reverse)
c = sum+difference
res = 0
for i in range(2,int(math.sqrt(c))+1):
    if c%i == 0:
        res = "Not prime"
        break
    else:
        res = "prime"
print("Sum of digits",sum)
print("Reverse",reverse)
print("Difference",difference)
print("Final Result",c)
print(res)