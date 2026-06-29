'''
35. Find the first word that is a palindrome'''
s = input("Enter a word: ")
temp=""
for i in range(len(s)):
    if s[i]!=" ":
        temp+=s[i]
    else:
        if  temp[::]==temp[::-1]:
            print(temp)
            temp=""
            break
        else:
            temp=""

if  temp !=" " and temp[::]==temp[::-1]:
    pass
    print(temp)

'''
s = input("Enter a word: ")

temp = ""
found = False

for i in range(len(s)):

    if s[i] != " ":
        temp += s[i]

    else:

        if temp == temp[::-1]:
            print(temp)
            found = True
            break

        temp = ""

if found == False and temp == temp[::-1]:
    print(temp)
    '''