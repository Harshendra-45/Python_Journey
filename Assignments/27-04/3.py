'''
3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35'''
n,m = map(int,input("Enter any num: ").split())
#for loop
# for i in range(n,m+1):
#     if i%10==5:
#         print(i,end=" ")

#while loop
while n<m:
    if n%10==5:
        print(n,end=" ")
    n+=1
    