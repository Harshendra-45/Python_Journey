'''
30) Extended Slanted Star Block
    **
     **
      **
       **
        **'''

n = int(input("Enter a no: "))
i = 1

while i<=n:
    r = (i*2)-(i+1)
    print()
    k = 1
    while k<=r:
        print(" ",end="")
        k+=1
    j=1
    while j<=n:
        print("*",end="")
        j+=1  
     
    i+=1