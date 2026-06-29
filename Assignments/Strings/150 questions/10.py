'''
10. Trim leading, trailing, or extra spaces from a string.'''
s = input("Enter a string: ")

res = ""

for i in range(len(s)):

    if s[i] == " " and (i == 0 or s[i-1] == " "):
        pass

    else:
        res += s[i]

if res != "" and res[-1] == " ":
    res = res[:-1]

print(res)