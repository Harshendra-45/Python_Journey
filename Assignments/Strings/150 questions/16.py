'''
Count total occurrences of a character. S = "programming", Char = 'g' 2
'''
s = input("Enter a string: ")
char = input("Enter a char: ")
count=0
for i in s:
    # print(i)
    if i==char:
        count+=1
print(char,count)