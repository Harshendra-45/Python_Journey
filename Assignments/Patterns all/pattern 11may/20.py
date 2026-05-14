n = int(input("Enter a no: "))
num = 1
for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
    
    
for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        
        start_num = (i * (i - 1)) // 2 + 1
        for j in range(i):
            print(start_num, end=" ")
            start_num += 1
        print()