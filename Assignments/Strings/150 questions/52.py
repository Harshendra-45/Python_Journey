'''Remove all special characters.'''
s = input("Enter a string: ")
res=""
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9':
            res+=i
print(res)