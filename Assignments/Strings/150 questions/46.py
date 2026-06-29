'''Check if a substring appears at both the start and end.'''
s = input("Enter a string: ")
word=input("Enter word: ")
flag = False
t = len(s)-len(word)
if len(s)>=len(word):
    temp=""
    for i in range(len(word)):
        temp+=s[i]
    if word==temp:
        start= True
if len(s)>=len(word):
    temp=""
    for i in range(t,len(s)):
            temp+=s[i]
    if word==temp:
         end=True

print("Start",start,"and","end",end)