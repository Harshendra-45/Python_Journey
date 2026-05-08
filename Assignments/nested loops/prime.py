'''
3.
Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47'''
import math
n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))
while n<m:
    i = 2
    if n>1:
        while i<=int(math.sqrt(n)):
            if n%i==0:
                break
            i+=1
        else:
            print(n)
    n+=1