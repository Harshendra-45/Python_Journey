'''
Fibonacci Series Generator

A learning app helps students understand number patterns. 
One of the most important patterns is the Fibonacci series, where each number is the sum of the previous two numbers.

The series starts with:
0 1

Write a program to:

- Read a number n (number of terms)
- Print the Fibonacci series up to n terms using a loop

Input:
7

Output:
0 1 1 2 3 5 8
'''
n = int(input("enter a no: "))
sum = 0
z = 0
# for i in range(0,n+1):
#     sum+=i
#     print(sum,end=" ")
prev = 0
i = 0
while i<n+1:
    sum = z+prev
    print(sum,end=" ")
    prev = sum
    i+=1