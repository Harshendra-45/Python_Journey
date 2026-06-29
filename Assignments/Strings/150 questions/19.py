'''
19. Find the highest frequency character in a string.
'''
st = input("Enter a string: ")
max = 0
res=""
for i in range(len(st)):
    count=0
    word = st[i]
    for j in range(len(st)):
        if st[j]==word:
            count+=1
    if count>max:
        max=count 
        res=""
        res+=st[i]
print(res)
    
