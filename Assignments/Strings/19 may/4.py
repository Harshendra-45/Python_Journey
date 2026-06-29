'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop'''
msg = input("Enter a msg: ")
# print(len(msg))
res =""
temp =""
for x in range(0,len(msg)):
    # print(temp)
    if msg[x]!=" " and msg[x:].isalnum():
        temp+=msg[x:]
        # print(temp)
        for i in range(len(temp)-1,-1,-1):
            # print(temp[i])
            res = res+temp[i]
        temp=""
        res+=" "
        break
    elif msg[x]==" ":
        # print(len(temp))
        for i in range(len(temp)-1,-1,-1):
            # print(temp[i])
            res = res+temp[i]
        temp=""
        res+=" "
    else:
        temp+=msg[x]
        # print(temp)
print(res)

''' More easy approach'''
'''
s=input("Enter a string: )
word=""
i=0
while i<len(S):
    if s[i]!=" ":
        word=s[i]+word
    else:
        print(word,end=" ")
        word=""
    i+=1
print(word,end=" ")
'''