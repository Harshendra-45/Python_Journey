'''
25. Count total number of words in a string.'''
s = input("Enter a string: ")

count = 0

for i in range(len(s)):

    if s[i] != " ":

        if i == 0 or s[i-1] == " ":
            count += 1

print(count)