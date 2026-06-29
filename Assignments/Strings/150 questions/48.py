'''Remove all vowels.'''
s = input("Enter a string: ")
res=""
for i in s:
    print(i)
    if i == 'a' or i== 'e' or i== 'i' or i== 'o' or i== 'u' or i== 'A' or i=='E' or i=='I' or i=='O' or i=='U':
        pass
    else:
        res+=i
print(res)
