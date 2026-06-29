'''
 Advanced Student Registration Data Processing System

A national university is developing an intelligent registration portal.
Students enter registration codes using uppercase letters, lowercase
letters, digits, and special symbols. Due to inconsistent data entry,
the administration wants the system to standardize and process the
information before storing it.

Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate
alphabets and digits - Convert all alphabets to lowercase - Remove
duplicate alphabets - Arrange alphabets in ascending order - Arrange
digits in descending order - Display alphabets first and digits later -
If no digits are found, display “No Digits Found”

Test Case 1 Input: Enter registration code: zBc@638

Output: Result: bcz863

Test Case 2 Input: Enter registration code: 5Br$dE654b

Output: Result: bder6554

Test Case 3 Input: Enter registration code: A9@C3d#6B1a

Output: Result: abcd9631

Test Case 4 Input: Enter registration code: X#X@M2A4x7

Output: Result: amx742

Test Case 5 Input: Enter registration code: r@T#y

Output: Result: rty No Digits Found
'''
code = input("Enter registration code: ").lower()
alpha =""
digit=""
result=""
for x in range(0,len(code)):
    if code[x].isalpha():
        alpha+=code[x]
    elif code[x].isdigit():
        digit+=code[x]
    
# print("alpha =", alpha)
# print("digit =", digit)
sort_alpha=sorted(alpha)
sort_num=sorted(digit)
sort_digit=sort_num[::-1]
for i in range(0,len(sort_alpha)):
    if i==0:
        result+=sort_alpha[i]
    elif sort_alpha[i]==sort_alpha[i-1]:
        pass
    else:
        result+=sort_alpha[i]
for i in range(0,len(sort_digit)):
    if i==0:
        result+=sort_digit[i]
    elif sort_digit[i]==sort_digit[i-1]:
        pass
    else:
        result+=sort_digit[i]
print(result)
if digit=="":
    print("No digits found")