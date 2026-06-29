'''Count vowels and consonants.'''

s = input("Enter a string: ")
alpha = 0
conso = 0

for i in s:
    if 'a'<=i<='z':
        alpha+=1
    elif '0'<=i<='9':
        digit+=1
    else:
        special+=1
print("Alphabets",alpha,"Digits",digit,"Special",special)
