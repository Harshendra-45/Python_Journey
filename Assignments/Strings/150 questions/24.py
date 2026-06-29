'''
24. Check if all characters in a string are unique (no repetition)'''
s = input("Enter a string: ")
res = True
for i in range(len(s)):
    count=0
    word = s[i]
    for j in range(len(s)):
        if s[j]==word:
            count+=1
    if count!=1:
        res=False
        break
print("yes")if res==True else print("no")



'''
s = input("Enter a string: ")

unique = True

for i in range(len(s)):

    for j in range(i+1, len(s)):

        if s[i] == s[j]:
            unique = False
            break

    if unique == False:
        break

print("yes") if unique else print("no")'''