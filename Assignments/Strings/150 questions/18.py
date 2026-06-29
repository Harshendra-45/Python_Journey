'''
18. Replace the first, last, or all occurrences of a character'''
s = input("Enter a string: ")
char = input("Enter char: ")
new = input("Enter char to replace: ")
res =""
for i in range(len(s)):
    if s[i]==char:
        res+=new
    else:
        res+=s[i]
print(res)