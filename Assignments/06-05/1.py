'''
1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions
'''
import math
while True:
    print("Menu Options:")
    print("1 → Check Prime Number")
    print("2 → Check Palindrome Number")
    print("3 → Reverse a Number")
    print("4 → Count Digits")
    print("5 → Exit")
    c = int(input("Enter choice: "))
    match c:
        case 1:
            import math
            n = int(input("Enter a num: "))
            for i in range(1,int(math.sqrt(n)-1)):
                if n%i==0:
                    print("Not prime")
                    break
            else:
                print("Prime")
        case 2:
            n = int(input("Enter a num: "))
            b = n 
            rev = 0
            for i in range(1,len(str(n))+1):
                c = n%10
                rev = rev*10+c
                n=n//10
            if rev==b:
                print("Palindrome number")
            else:
                print("not palindrome")
        case 3:
            n = int(input("Enter a num: "))
            rev = 0
            for i in range(1,len(str(n))+1):
                c = n%10
                rev = rev*10+c
                n=n//10
            print(rev)
        case 4:
            n=int(input("enter a no: "))
            count = 0
            for i in range(1,len(str(n))+1):
                   count+=1 
            print(count)
        case _:
            print("Invalid choice")