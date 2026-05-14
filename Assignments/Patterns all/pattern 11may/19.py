'''
19) Reverse Number Cross
    5   5
     4 4
      3
     4 4
    5   5
'''
n = int(input("Enter a number: "))
i = 1
j = n
k = 0
z = j-k
while i<=n:
    print()

    while z>=n:
        
        z = j-k
        if i%2!=0 and z%2!=0: 
            print(z,end="")
            
        elif i%2==0 and z%2==0:
            print(z,end="")
            
        elif i%2!=0 and z>=2:
            print(z,end=" ")
            
        else:
            print(" ",end="")
        j-=1
    i+=1