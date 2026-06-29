'''2.

=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza

---'''
orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

dc={}
for i in orders:
    f = orders.count(i)
    if i not in dc:
        dc[i]=f
print(dc)
highest_ordered = max(dc, key=dc.get)
print("Most ordered",highest_ordered)