'''
23. Print all characters that occur exactly twice.'''
s = input("Enter a string: ")
res=""
for i in range(len(s)):
    count=0
    word = s[i]
    for j in range(len(s)):
        if s[j]==word:
            count+=1
    if count==2:
        if s[i] not in res:
         res+=s[i]
print(res)