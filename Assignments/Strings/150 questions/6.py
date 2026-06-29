'''
6. Convert a string to uppercase'''
s=input("Enter a string: ")
res=""
for i in s:
    if 'a'<=i<='z':
        res+=chr((ord(i)-32))
    else:
        res+=i
print(res)