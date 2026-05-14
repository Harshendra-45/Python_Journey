'''
*
##
***
####
*****
'''
n = int(input("Enter a num: "))
i = 1
while i<=n:
    j = 1
    while j<=i:
        if i%2==0:
            print("#",end="")
        else:
            print("*",end="")
        j+=1
    i+=1
    print()