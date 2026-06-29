'''6.
note: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.
Tuple Format:
(product_id, product_name, price)
Requirements:
Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.
Test Case:
Input:
Enter number of products: 4
P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000
Expected Output:
All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)
Costliest Product:
('P103', 'Television', 80000)
Cheapest Product:
('P102', 'Mobile', 25000)
Average Price:
50000.0
Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)
'''
n = int(input("Enter no of products: "))
product = []
for i in range(n):
    id = input("Enter product id: ")
    name = input("Enter product name: ")
    cost = float(input("Enter product cost: "))
    product.append(tuple([id,name,cost]))

for u in product :
    print(u)

max = product[0]
for i in product:
    if i[2]>max[2]:
        max = i
print("costliest product", max)
min = product[0]
for i in product:
    if i[2]<min[2]:
        min = i
print("cheapest product", min)
sum = 0
for z in product:
    sum+=z[2]
print("Average",sum/n)

for d in product:
    if d[2]>50000:
        print(d)
