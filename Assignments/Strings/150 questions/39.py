''' Search all occurrences of a character'''
word = input("Enter a string: ")
ch = input("Enter a char: ")
for i in range(len(word)):
    if ch==word[i]:
        print(i,end=" ")