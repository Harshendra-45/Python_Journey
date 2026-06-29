'''
. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:

```
Python is powerful
```

Output:

```
lufrewop si nohtyP
```'''
s = input("Enter any no: ")
key = s.split()
rev=""
i = len(key)-1
while i>=0:
    word = key[i]
    j=len(word)-1
    while j>=0:
        rev+=word[j]
        j-=1
    i-=1
    word=""
    rev+=" "
print(rev)
