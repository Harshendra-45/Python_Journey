'''Check if two strings are rotations of each other'''
s = input("Enter a string: ")
s1 = input("Enter a string: ")
if len(s)==len(s1) and s1 in (s+s):
    print(True)
else:
    print(False)