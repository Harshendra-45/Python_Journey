'''
17. Remove the first, last, or all occurrences of a given character
'''
s = input("Enter a string: ")
char = input("Enter char: ")
res =""
for i in range(len(s)):
    if s[i]==char:
        continue
    else:
        res+=s[i]
print(res)