'''QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
'''
from collections import namedtuple
customer = namedtuple("customer",["id","name","prname","amt"])
n = int(input("Enter a no:"))
clist = []
for i in range(n):
    id = (input("Enter id: "))
    name = (input("Enter name: "))
    pr_name = input("Enter product name: ")
    amount = int(input("Enter amount: "))
    clist.append(customer(id,name,pr_name,amount))

for i in clist:
    print(i)
max = clist[0]
for i in clist:
    if i.amt>max.amt:
        max=i
print(max)
sales = 0
for i in clist:
    sales+=i.amt
print("Total sales",sales)

c=0
for i in clist:
    if i.amt>10000:
        c+=1
print("Orders above 10k = ", c)