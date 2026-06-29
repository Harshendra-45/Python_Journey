a = [8,10,6,12]
max = int(a[0])
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
print(max)