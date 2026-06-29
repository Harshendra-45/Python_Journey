'''check if two strings are anagrams. '''
s1 = input("Enter a string: ")
s2 = input("Enter a string: ")
if len(s1)==len(s2) and sorted(s1)==sorted(s2):
    print("Valid")
else:
    print("Invalid")