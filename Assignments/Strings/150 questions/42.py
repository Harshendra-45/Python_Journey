''' 42. Check if two strings are equal without equals().'''
st1 = input("Enter a string: ")
st2 = input("Enter a string: ")
found=0
if len(st1)==len(st2):
    for i in st1:
        for j in st2:
            if i==j:
                found=1
            else:
                found=0
else:
    found=0

if found==1:
    print("Equal")
else:
    print("Not equal")
  
   
    