n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))
while n<=m:
    b = n
    sum = 0
    while b>0:
        dig = b%10
        i = 1
        mul = 1
        while i<=dig:
            mul *=i
            i+=1
        sum+= mul
        b=b//10
    if sum == n:
        print(n)
    n+=1