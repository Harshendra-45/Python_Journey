'''
7. Convert a string to lowercase'''
s=input("Enter a string: ")
res=""
for i in s:
    if 'A'<=i<='Z':
        res+=chr((ord(i)+32))
    else:
        res+=i
print(res)