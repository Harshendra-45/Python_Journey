'''
30. Replace a word with another word.'''
s = input("Enter a string: ")
word = input("Enter a word to replace: ")
word2 = input("Enter new word: ")

res = ""
i = 0
while i < len(s):
    # Check if the word matches starting at current position
    if s[i:i + len(word)] == word:
        res += word2
        i += len(word)          # Important: skip the length of old word
    else:
        res += s[i]
        i += 1                  # move only one character

print(res)