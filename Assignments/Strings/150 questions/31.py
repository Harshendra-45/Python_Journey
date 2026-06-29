'''
31. Remove duplicate words from a string.'''
'''31.Remove duplicate words.'''

s = input("Enter string: ")
l = s.split()

result = ""

for i in range(len(l)):

    if l[i] not in l[:i]:
        result += l[i] + " "

print("Result:", result)