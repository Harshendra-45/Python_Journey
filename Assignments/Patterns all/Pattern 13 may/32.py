'''
55555
4444
333
22
1
'''
n = int(input("Enter a num: "))
i = 1
k = n
while i<=n:
    
    j = n
    while j>=i:
        print(k,end="")
        
        j-=1
    i+=1
    k-=1
    print()