'''
*****
####
***
##
*
'''
n = int(input("Enter a no: "))
i = 1
while i<=n:
    j = n
    while j>=i:
        if i%2!=0:
            print("*",end="")
        else:
            print("#",end="")
        j-=1
    i+=1
    print()