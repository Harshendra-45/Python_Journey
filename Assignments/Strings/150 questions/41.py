'''41. Check if a string contains a substring (without using contains()).'''
string = input("Enter a string: ")
word = input("Enter word to search: ")
temp=""
flag=False
count=0
for i in range(len(string)-len(word)+1):
    if string[i]==word[0]:
        for j in range(len(word)):
            if string[i+j]!=word[j]:
                flag = False
                break
        else:
                flag=True
                count+=1
                # print(i,end=" ")

if flag==True:
     print(True)
else:
     print(False)
print(count)