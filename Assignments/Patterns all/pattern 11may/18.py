'''
18) Binary Floyd Triangle
    1
    0 1
    1 0 1
    0 1 0 1
'''
n = int(input("enter a no: "))
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        print(0,end="") if(( i%2==0 and j%2!=0)or( i%2!=0 and j%2==0)) else print(1,end="")
        # print(0,end="") if  j%2!=0 else print(1,end="")
