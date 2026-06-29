'''32. Count the frequency of each word in a string'''
s = input("Enter string: ")
l = s.split()

words = []

for i in range(len(l)):

    if l[i] not in words:

        count = 0

        for j in range(len(l)):

            if l[i] == l[j]:
                count += 1

        print(l[i], ":", count)

        words.append(l[i])