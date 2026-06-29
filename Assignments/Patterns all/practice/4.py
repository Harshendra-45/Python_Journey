k = int(input("Enter a no: "))
for b in range(1,k+1):
    ch=65
    print()
    for c in range(1,k-b+1):
        print(" ",end="")
    breaks = (2*b)//2
    for d in range(1,2*b):
        print(chr(ch),end="")
        if d<breaks:
            ch+=1
        else:
            ch-=1
    for e in range(1,k-b+1):
        print(" ",end="")
    