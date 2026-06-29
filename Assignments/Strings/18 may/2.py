'''
2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12
'''
mob_no =input("Enter contact number: ")
digit = 0
for i in mob_no:
    if '0'<=i<='9':
        digit+=1
print("Total Digits:",digit)