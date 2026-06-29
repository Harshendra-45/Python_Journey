'''
21. Find the first non-repeating character.
'''
s = input("Enter a string: ")
for i in range(len(s)):
    count=0
    word = s[i]
    for j in range(len(s)):
        if s[j]==word:
            count+=1
    if count==1:
        print(s[i])
        break
