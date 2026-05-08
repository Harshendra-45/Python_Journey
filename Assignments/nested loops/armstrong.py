'''
4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407'''
n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))
while n<=m:
    sum = 0
    temp = n
    count = len(str(n))
    while temp>0:
        dig = temp%10
        sum = sum + (dig**count)
        temp //=10
    if n==sum:
        print(n)
    n+=1
