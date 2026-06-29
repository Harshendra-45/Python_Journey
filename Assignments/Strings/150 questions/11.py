'''
11. Get the character at a given index.'''
s=input("Enter a string: ")
index = int(input("Enter string index: "))
for i in range(0,len(s)):
    if i==index:
        print(s[i])
        break