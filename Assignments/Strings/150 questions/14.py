'''
14. Find the first occurrence of a character in a string'''
s=input("Enter a string: ")
ch=input("Enter character to find: ")
for i in range(0,len(s)):
    if s[i]==ch:
        print(s[i],i)
        break