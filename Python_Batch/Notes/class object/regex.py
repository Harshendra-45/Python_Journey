import re

# txt = "The rain in Spain"

# # Evaluates the pattern and returns a Match object if successful
# x = re.search("^The.*Spain$", txt)

# if x:
#     print("YES! We have a match!")
#     print(f"Matched text: {x.group()}")
#     # print(f"Character span: {x.span()}")
#     print(x)
# else:
#     print("No match")


#Findall
#

# Search 
# txt = "The rain in Spain"
# x=re.search("\s",txt)
# print("first white space character at ", x.start())

#split
# txt = "The rain in Spain"
# x=re.split("\s",txt)
# print(x)

#sub()
# txt = "The rain in Spain"
# x=re.sub("\s","9",txt)
# print(x)

#Sub for first two occurences
# txt = "The rain in Spain"
# x=re.sub("\s","",txt,2)
# print(x)

#Returns an iterator of Match objects.
text = "cat bat rat"
res = re.finditer("at",text)
#print(res)re.finditer() does not return the matches immediately.
for i in res:
   print(i.string)

#To get the position of each match
# text = "cat bat rat"
# res = re.finditer("at",text)
# for i in res:   
#    print(i.group())

#To get the position of each match
# text = "cat bat rat"
# res = re.finditer("at",text)
# for i in res:
#     print(i.group(), i.start(), i.end())

#Match objects
# txt = "The rain in Spain"
# x=re.search("ai",txt)
# print(x)
#.span()
# txt = "The rain in Spain"
# x=re.search(r"\bS\w+",txt)
# print(x.span())