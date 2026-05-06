'''6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2'''



count = 0
smallest = None
num = int(input("Enter Number = "))

if num<=1:
    print("Not a Composite Number")
    print("Factors Count = 0")
    print("Smallest Factor = None")
else:
    for i in range(1,num+1):
        if num%i==0:
            count+=1
            if i>1 and smallest is None:
                smallest = i
if count>2:
    print("Composite Number")
    print("Factors =",count)
    print("Smallest =",smallest)