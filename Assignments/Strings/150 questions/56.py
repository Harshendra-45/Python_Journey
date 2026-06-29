'''Reverse only consonants.'''
s = input('Enter a string: ')
res=""
cos =""
for ch in s:
    if ch not in "aeiouAEIOU" and ch not in "0123456789":
        cos+=ch
print(cos)
revcos = cos[::-1]
i = 0
for z in s:
   if z=='a' or z=='e' or z=='i' or z=='o' or z=='u' or '0'<=z<='9':
       res+=z
       
   else:
       res+=revcos[i]
       i+=1
print(res)