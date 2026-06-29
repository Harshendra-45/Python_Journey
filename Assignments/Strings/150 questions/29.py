'''29. Remove occurrences of a word.'''
# Doubt
s = input("Enter a string: ")
word = input("Enter a word: ")

res = ""

i = 0

while i < len(s):

    match = True

    if i + len(word) <= len(s):

        for j in range(len(word)):

            if s[i+j] != word[j]:
                match = False
                break

        if match:
            i += len(word)
            continue

    res += s[i]
    i += 1

print(res)