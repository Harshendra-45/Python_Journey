'''
WAP to find out all the leap years between two entered years
'''
n = int(input("Enter a no:"))
m = int(input("Enter a no:"))
while n<=m:
    if n%100==0:
        if n%400==0:
           
         print(n)
    else:
        if n%4==0:
            print(n)
    n+=1