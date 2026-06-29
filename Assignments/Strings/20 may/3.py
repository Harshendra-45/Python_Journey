'''
. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:

```
e
```'''
s = input("Enter a string: ")
for i in range(1,len(s)):
    count=0
    f=0
    for j in range(i+1,len(s)):
        if count(s[i])!=count(s[j]):
            print(i)
            break 
    j+=1
    i+=1
if f==0:
    print("No Char found")