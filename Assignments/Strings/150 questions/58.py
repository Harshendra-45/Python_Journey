'''Rotate characters by 2 positions to the left. '''
s = input("Enter a string: ")
n = int(input("Enter rotation no: "))
if s=="":
    res=""
else:
    if n>len(s):
        rot = n%len(s)
    else:
        rot=n
    res="" 
    temp=""
    for i in range(len(s)):
        if i<=rot-1:
            temp+=s[i]

        else:
            res+=s[i]
    res+=temp
print(res)
