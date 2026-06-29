'''Remove all punctuation characters. '''
s = input("Enter a string: ")
res=""
for i in s:
    if i not in ("." ,',',  '!',  '?',  ';',  ':',  "'", "_", ' _' , '( )' , '[ ]' ,  '{ }','"'):
        res+=i
print(res)