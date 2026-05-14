'''
a
ab
abc
abcd
abcde

'''
n = int(input("Enter a no: "))
for i in range(1,n+1):
    ch = 97
    for j in range(1,i+1):
        print(chr(ch),end="")
        ch+=1
    print()