'''Replace all duplicate characters with '$'. '''
s = input("Enter a string: ")
res=""
for i in s:
    if i not in res:
        res+=i
    else:
        res+='$'
print(res)