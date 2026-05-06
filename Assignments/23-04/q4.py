'''
4. Reverse a Number
A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to *reverse a given integer using loops*.

Input: 1234
Output: 4321
'''

num = int(input("Enter a number: "))
while num>0:
    dig = num%10
    print(dig, end="")
    num = num//10
    
    
print("\nDone")


# num = int(input("Enter a number: "))
# for i in range(num):
#     dig = num%10
#     print(dig,end="")
#     num = num//10
#     