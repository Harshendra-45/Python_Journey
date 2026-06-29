'''
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy'''
msg = input("Enter a name: ")
msg1 =""
for x in range(0,len(msg)):
    if msg[x]==" " and msg[x-1]==" ":
            msg1 = msg1
    else:
            msg1+=msg[x]
print(msg1)