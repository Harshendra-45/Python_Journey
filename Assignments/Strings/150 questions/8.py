'''
8. Toggle the case of each character in a string.'''
s=input("enter a string: ")
res=""
for i in s :
    if 'a'<=i<='z':
        res+=chr(ord(i)-32)
    elif 'A'<=i<='Z':
        res+=chr(ord(i)+32)
    else:
        res+=i
print(res)