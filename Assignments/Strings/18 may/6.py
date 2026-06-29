'''
5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
'''
Product_code= input("Enter product code: ")
rev = ""


for i in range(len(Product_code)-1,-1,-1):
    rev+=Product_code[i]
print(rev)
if rev==Product_code:
    print("Palindrome")
else:
    print("noT ")    


# if Product_code[::]==Product_code[::-1]:
#     print("Palindrome code")
# else:
#     print("Not a Palindrome Code")