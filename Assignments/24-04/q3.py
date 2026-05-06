'''

3. First Digit of Number
A university receives thousands of application IDs. 
The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5
'''
# method 1
num = int(input("Enter applic. ID: "))
i = 0
while num>0:
    dig=num%10
    i=dig
    num=num//10 
print(i)

#method 2
# num = input("Enter applic. ID: ")
# i = 0
# for i in num :
#     print(i)
#     if int(i)>1:
#         break
