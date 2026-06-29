''' Search all occurrences of a word.'''
string = input("Enter a string: ")
word = input("Enter word to search: ")
temp=""
for i in range(len(string)-len(word)+1):
    if string[i]==word[0]:
        for j in range(len(word)):
            if string[i+j]!=word[j]:
                break
        else:
                print(i,end=" ")

