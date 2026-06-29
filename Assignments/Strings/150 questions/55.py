'''Reverse only vowels '''
s = input('Enter a string: ').lower()
res=""
vow =""
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vow+=i
print(vow)
revvow = vow[::-1]
i = 0
for z in s:
   if z=='a' or z=='e' or z=='i' or z=='o' or z=='u':
       res+=revvow[i]
       i+=1
   else:
       res+=z
print(res)