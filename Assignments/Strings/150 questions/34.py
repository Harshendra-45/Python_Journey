'''
34. Find the shortest word in a string.'''


s = input("Enter a string: ")
res = s[0:]
temp = ""

for i in range(len(s)):

    if s[i] != " ":
        temp += s[i]

    else:

        if temp != "":

            if len(temp) < len(res):
                res = temp

            temp = ""

if temp != "" and len(temp) < len(res):
    res = temp

print(res)