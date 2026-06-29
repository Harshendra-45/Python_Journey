'''
33. Find the longest word in a string'''
# s = input("Enter a string: ")
# l = s.split()
# max=0
# res=""
# for i in l:
#     if len(i)>max:
#         max=len(i)
#         res=i
# print(res)


s = input("Enter a string: ")
res = ""
temp = ""
for i in range(len(s)):
    if s[i]!=" ":
        temp+=s[i]
    else:
        if len(temp)>len(res):
            res= temp
            temp=""
if len(temp)>len(res):
    res= temp
print(res)

