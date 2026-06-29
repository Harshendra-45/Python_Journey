# 3. Reverse Words Without split()

s = input("Enter sentence: ")

word = ""
result = ""

for i in range(len(s)-1, -1, -1):

    if s[i] != " ":
        word = s[i] + word

    else:
        result += word + " "
        word = ""

result += word

print(result)