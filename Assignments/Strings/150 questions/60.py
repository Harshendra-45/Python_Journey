'''Append two strings but remove duplicate adjacent characters. '''
s = input("Enter a string: ")
s1 = input("Enter a string: ")

g = s+s1
res=""
for i in range(len(s+s1)):
    if i==0:
        res+=  g[i]
    elif i>=1:
        if g[i-1]==g[i]:
            pass
        else:
            res+=g[i]
print(res)
