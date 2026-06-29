'''=========================================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6

--- '''
n = int(input("Enter no of items: "))
d ={}
for i in range(n):
    key=input("Enter key")
    value=int(input("Enter value"))
    d[key]=value
print(d)
quan=sum(d.values())
print("Total quantity",quan)