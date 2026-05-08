'''
10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students.
The administration wants to verify IDs by checking how many odd digits are present in each ID number. 
IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 3
'''
# n = int(input("Enter a num: "))
# count = 0
# for i in range(0,n//2):
#     if i%3==0:
#         count+=1
# print("Odd Digits Count =",count)        

n = input("Enter a num: ")
count = 0
for i in range(0,len(n)+1):
    if int(i)%3==0:
        count+=1
print("Odd Digits Count =",count)        