'''36. Reverse the order of words in a string.'''
# s = input("Enter a string: ")
# res=""
# temp=""
# for i in range(len(s)):
#     if s[i]!=" ":
#         temp+=s[i]
#     else:
#         if temp!="":
#             res=temp+" "+res
#             temp=""

# if temp!="":
#     res=temp+" "+res
# print(res)



''' s = input("Enter a string: ")

res = ""
temp = ""

for i in range(len(s)):

    if s[i] != " ":
        temp += s[i]

    if s[i] == " " or i == len(s)-1:

        if temp != "":
            res = temp + " " + res

        temp = ""

print(res)'''

s = input("Enter a string: ")
m = s.split()
res=""
for i in m:
    res=i+ " "+res
print(res)
