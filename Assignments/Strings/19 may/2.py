'''2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST
'''
name = input("Enter a name: ")
sid =""
for x in range(0,len(name)):
    if x==0:
        if name[x]!=" " :
            sid+=chr(ord(name[x])-32)
    elif name[x]!=" " and name[x-1]==" ":
        sid+=name[x]
        sid+=chr(ord(name[x])-32)
print(sid)