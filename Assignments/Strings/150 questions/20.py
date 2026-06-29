'''20. Find the lowest frequency character in a string.'''
st = input("Enter a string: ")
min = len(st)
res=""
for i in range(len(st)):
    count=0
    word = st[i]
    for j in range(len(st)):
        if st[j]==word:
            count+=1
    if count<min:
        min=count 
        res=""
        res+=st[i]
print(res)
    