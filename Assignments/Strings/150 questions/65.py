'''Count palindromic substrings. '''
s = input("Enter a string: ")
res2 = []
for i in s :
    res2.append(i)


for i  in range(1,len(s)-1):

    
    if i>=2 and i<len(s)-2:
        if s[i-2]==s[i+2] and s[i-1]==s[i+1]:
            res2.append((s[i-2:i+3]))
    elif s[i-1]==s[i+1]:
        res2.append((s[i-1:i+2]))
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        if i>=1 and i<=len(s)-2:
            if s[i-1]==s[i+2]:
                res2.append((s[i-1:i+3]))
        else:
            res2.append((s[i:i+2]))




print(res2)


