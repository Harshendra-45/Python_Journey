'''
2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5'''
st = input("Enter chat message: ")
count=0
# i = 0
# while i<len(st):
#     ch=st[i]
#     if ch==" ":
#         count+=1
#     i+=1
# print("Total spaces", count)
for ch in st:
    if ch==" ":
        count+=1
print("Total spaces",count)