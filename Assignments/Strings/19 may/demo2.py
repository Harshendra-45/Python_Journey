'''
'''
s = input("enter a string: ")
word=""
short=""
for i in range(0,len(s)):
    if i==" ":
        word+=s[:i]
        short=word
    elif i!=" ":
        word+=s[i]
    else:
        if short>word:
            short=word
        else:
            short=short
print(short)