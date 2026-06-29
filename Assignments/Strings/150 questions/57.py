'''Merge two strings alternatively (char by char). '''
s = input("enter a string: ")
s1 = input("enter a string: ")
res=""
for i in range(min(len(s1),len(s))):
    
        res+=s[i]
        res+=s1[i]
        if i==min(len(s1),len(s))-1:
            res+=s[i+1:]
            res+=s1[i+1:]
print(res) 