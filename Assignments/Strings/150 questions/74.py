''' Find the longest substring without repeating characters.'''
s = input("Enter a string: ")
res=""
temp=""
for i in s:
    if i not in temp:
        temp=temp+i
        # print(temp)
    else:
        if len(temp)>len(res):
         res=temp
        temp = temp[temp.find(i)+1:]
        temp= temp+i
        #  print(temp)
    if len(temp)>len(res):
        res = temp


print(res)
print(len(res))