'''
Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29
'''
n = int(input("Enter a number: "))
b = n
for i in range(b+1,b*2+1):
    n+=1
    if n%i//2==0:
        pass
    elif n%i!=0:
        print(n)
        break
