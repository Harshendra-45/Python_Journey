'''
1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''
user = input("Enter username: ")
letter = 0
space = 0
rem = 0
if 5<=len(user)<=12:
    for i in range(0,len(user)):
        if  i==0 and ('a'<=user[i]<='z' or 'A'<=user[i]<='Z'):
            letter=1
        elif user[i]==" ":
            space=1
        elif i>=1:
            if'0'<=user[i]<='9' or 'a'<=user[i]<='z' or 'A'<=user[i]<='Z' or user[i]=="_":
                rem=1
            else:
                 rem=0
                 break
        
# print(letter)
# print(rem)
# print(space)

if letter==1 and space==0 and rem>=1:
    print("Valid Username")
else:
    print("Invalid username")