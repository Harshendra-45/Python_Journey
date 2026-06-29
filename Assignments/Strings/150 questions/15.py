'''
15. Find the last occurrence of a character in a string.'''
s=input("Enter a string: ")
ch=input("Enter character to find: ")
for i in range(len(s)-1,-1,-1):
    if s[i]==ch:
        print(s[i],i)
        break