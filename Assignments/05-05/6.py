# 6.
# Data Validation System – Character Identifier
# A system needs to validate user input characters.
# If the input is:
# Alphabet → display "Alphabet"
# Digit → display "Digit"
# Otherwise → display "Special Character"
# Write a program using inline if to classify the character.

a=input("enter the input ")
# print(ord("0"))     -48
# print(ord("9"))     -57
# print(ord("A"))     -65
# print(ord("Z"))     -90
# print(ord("a"))     -97
# print(ord("z"))     -122

for i in a:
    x=ord(i)
    # print("alphabet" if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) else "digit" if ord(i)>=48 and ord(i)<=57 else "special characters")
    print("alphabet" if (x>=65 and x<=90) or (x>=97 and x<=122) else "digit" if x>=48 and x<=57 else "special characters")