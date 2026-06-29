'''
123456
54321
1234
321
12
1
'''

n = int(input("Enter a no: "))

for i in range(1,n+1):
    od = n-i+1
    ev = 1
    for j in range(n,i-1,-1):
        if i%2==0:
            print(od,end="")
            od-=1
        else:
            print(ev,end="")
            ev+=1
    
    print()