'''Extract only digits.'''
s = input("Enter a string: ")
res=""
for i in s:
    if ("0"<=i<="9"):
        res+=i
print(res)