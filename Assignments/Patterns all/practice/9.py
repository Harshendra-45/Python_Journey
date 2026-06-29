# 1. First Non-Repeating Character

s = input("Enter string: ")

for i in range(len(s)):

    count = 0

    for j in range(len(s)):

        if s[i] == s[j]:
            count += 1

    if count == 1:
        print("First Non-Repeating Character:", s[i])
        break
else:
    print("No unique character found")