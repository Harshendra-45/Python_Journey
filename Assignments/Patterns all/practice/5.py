n = int(input("Enter a no: "))
ch=65+n-1
for i in range(1,n+1):
    
    for j in range(1,i+1):
        print(chr(ch+j-1),end=" ")
        
    ch-=1
    print()