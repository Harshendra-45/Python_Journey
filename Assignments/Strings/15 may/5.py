'''
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password'''
password = input("Enter password: ")
i = 0
first = 0
last = 0
count=0
space = 0
sp = 0
valid = 0
if 8<=len(password)<=15:

    while i<len(password):
        ch = password[i]
        if i==0:
            if ch.isupper():    
                first += 1
        elif i==len(password)-1:
                if ch.isdigit():
                    last += 1
                    count+=1
        elif "0"<=ch<="9":
            count+=1
        elif ch==" ":
            space+=1
        elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
             pass
        else:
            sp+=1
        i+=1
else:
     valid = 0


if first>=1 and last>=1 and count>=2 and space==0 and sp>=1:
     valid =    1

print("Secure Password ")if valid ==1 else print("Not valid")
#for debugging part
# print(first)
# print(last)
# print(count)
# print(space)
# print(sp)
        


            