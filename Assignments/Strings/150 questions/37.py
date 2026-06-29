'''
37. Reverse each word in a string.'''
s = input("Enter a string: ")
temp=""
res=""
for i in range(len(s)):
    if s[i]!=" ":
        temp+=s[i]
    if s[i] == " " or i == len(s)-1:
        
        if temp!="":
            j = len(temp)-1
            while j>=0:
                res+=temp[j]
                j-=1
            temp="" 
        res+=" "
print(res)
