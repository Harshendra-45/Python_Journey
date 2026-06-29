'''13. Get the Unicode code point before a given index.
'''
s=input("Enter a string: ")
index=int(input("Enter a index: "))
for i in range(0,len(s)):
    if i<=index:
        print(s[i], ord(s[i]))