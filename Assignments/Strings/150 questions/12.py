'''
12. Get the Unicode code point of a character at an index.'''
s=input("Enter a string: ")
index=int(input("Enter a index: "))
for i in range(0,len(s)):
    if i==index:
        print(s[i], ord(s[i]))