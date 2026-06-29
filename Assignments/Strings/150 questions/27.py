'''
27. Find the last occurrence of a word in a string.'''
s = input("Enter a string: ")
word = input("Enter a word : ")
res = None
for i in range(len(s)-len(word)+1):
    if s[i]==word[0]:
        for j in range(len(word)):
            if s[i+j]!=word[j]:
                break
        else:
            res = i
# print(s[26:])
print(res)