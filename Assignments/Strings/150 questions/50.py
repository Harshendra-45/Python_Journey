'''Remove all digits. '''
s = input("Enter a string: ")
res=""
for i in s:
    if '0'<=i<='9':
        pass
    else:
        res+=i
print(res)

'''if not ('0' <= i <= '9'):
    res += i'''