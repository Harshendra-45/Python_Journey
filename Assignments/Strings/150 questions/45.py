'''check whether a string starts/ends with another string. '''
s = input("Enter a string: ")
pre=input("Enter word: ")
ending =input("Enter word: ")
start=False
end = False
t = len(s)-len(ending)
if len(s)>=len(pre):
    temp=""
    for i in range(len(pre)):
        temp+=s[i]
    if pre==temp:
        start= True
if len(s)>=len(ending):
    temp=""
    for i in range(t,len(s)):
            temp+=s[i]
    if ending==temp:
         end=True

print("Start",start,"and","end",end)