'''
22. Find the last repeating character.'''
# s = input("Enter a string: ")
# res = ""
# for i in range(len(s)):
#     count=0
#     word = s[i]
#     for j in range(len(s)):
#         if s[j]==word:
#             count+=1
#     if count>1:
#         res=s[i]
        
# print(res)


#for last distinct character set 
s = input("Enter a string: ")
res = ""
char = ""
for i in range(len(s)):
    count=0
    word = s[i]
    for j in range(len(s)):
        if s[j]==word:
            count+=1
    if count>1:
        if s[i] in res:
            res=res
        else:
            res += s[i]
            char = s[i]
        
    
print(char)