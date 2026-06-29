'''
wap to reverse a string and word also'''
s=input()
words = s.split()
i=len(words)-1
while i>=0:
    word=words[i]
    rev=""
    j=len(word)-1
    while j>=0:
        rev+=word[j]
        j-=1
    print(rev,end=" ")
    i-=1
    
