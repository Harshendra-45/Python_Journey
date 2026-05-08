'''
2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
'''
import math
n = int(input("Enter a num: "))
sum = 0
product = 1
difference = 0
while n > 0:
    digit = n % 10
    sum += digit
    product *= digit
    n //= 10

difference = abs(sum-product)
count = len(str(difference))
f = difference+count
print("Sum of digits",sum)
print("product",product)
print("Difference",difference)
print("Count",count)
print("Final Result",f)
for i in range(2,int(math.sqrt(f)+1)):
    if f%i==0:
        print("Not Prime")
        break
    else:
        print("Prime")
        break