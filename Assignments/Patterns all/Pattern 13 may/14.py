'''
1
23
456
78910
'''
n = int(input("Enter a no: "))
count=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(count,end="")
#         count+=1
#     print()
i = 1
while i<=n:
    j=1
    while j<=i:
        print(count,end="")
        j+=1
        count+=1
    i+=1
    print()