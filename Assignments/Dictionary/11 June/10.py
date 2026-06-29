'''10.
=========================================
EMAIL DOMAIN COUNTER
====================
emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]

Write a program to:

* Count users belonging to each email domain.

Sample Output:
{
'gmail.com':3,
'yahoo.com':1,
'outlook.com':1
}

---'''
emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]
domain =[]
for i in range(len(emails)):
    temp = emails[i]
    res=""
    for j in range(len(temp)):

        if temp[j]=="@":
            for k in range(j,len(temp)):
             if temp[k]==".":
                break
             else:
                 res=temp[j+1:]
                #  print(j)
    domain.append((res[:-1]))
# print(domain)
dc = {}
for i in domain:
   c = domain.count(i)
   if i not in dc:
      dc[i]=c
print(dc)