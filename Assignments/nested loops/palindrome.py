'''6.Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191'''

sn = int(input("Enter starting number: "))
en = int(input("Enter ending number: "))
print("Palindrome Numbers are: ")
# rev = 0
# i=sn
# while i<0:
#     temp=i
#     r=temp%10
#     rev=rev*10+d
#     temp=temp//10

# i=sn
# while i<=en:
#     rev=0
#     j=i
#     while j>0:
#         mod=j%10
#         j=j//10
#         rev=(rev*10)+mod
#     if i==rev:
#         print(i)
#     i=i+1


while sn<=en:
    rev = 0
    j=sn
    while j>0:
        dig = j%10
        rev = (rev*10)+ dig
        j=j//10
    if sn == rev:
        print(sn)
    sn+=1


