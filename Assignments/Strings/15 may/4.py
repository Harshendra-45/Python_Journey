'''
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U
'''
string = input("Enter student name: ").lower()
count=0
for ch in string:
    if ch!="a"and ch!="i"and ch!="e" and ch!="o"and  ch!="u" and ch!=" ":
        count+=1
print("Total consonants",count)