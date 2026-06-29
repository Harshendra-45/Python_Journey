'''#list question 
friends = ["harsh","sahil", "anil", "daya"]
name = input("Enter name: ")
if name in friends:
    index=friends.index(name)
    friends[index]=name.upper()
    print(friends)
else:
    print("not found")'''

arr = [11,5,7,12,12,14,16]
arr1 = [11,2,12,14,16]
comm=[]
# even=[]
for i in arr:
    if i in arr1:
        if i%2==0 and i>10:
            comm.append(i)

print(comm)