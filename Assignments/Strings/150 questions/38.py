'''Reverse words without split().'''
'''
37. Reverse each word in a string.'''
s = input("Enter a string: ")
res=""
temp=""
for i in range(len(s)):
    if s[i]!=" ":
        temp+=s[i]
    else:
        if temp!="":
            res=temp+" "+res
            temp=""

if temp!="":
    res=temp+" "+res
print(res)

