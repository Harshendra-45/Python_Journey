'''
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
'''
n = int(input("Enter a number: "))
sum = 0
pr = 1
for i in range(0,len(str(n+1))):
    rem = n%10
    sum+=rem
    pr*=rem
    n=n//10

if sum==pr:
    print("Spy number")
else:
    print("Not a spy no.")