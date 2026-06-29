'''
1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc

'''
str = input("Enter a string: ")
word = ""
for i in range(0,len(str)):
        print(str[i])
        # print(word[i])
        if str[i]==word :
          pass
        else:
            word+=str[i]
            break
print(word)